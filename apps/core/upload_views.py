import pandas as pd
from django.core.files.storage import default_storage
from .uploads import DataUpload
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.core.models import Tenant
from apps.users.models import User

@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        upload_type = 'excel' if file.name.endswith(('.xls', '.xlsx')) else 'csv'
        tenant = request.user.tenant_memberships.first().tenant  # Simplified
        data_upload = DataUpload.objects.create(
            tenant=tenant,
            uploaded_by=request.user,
            upload_type=upload_type,
            file=file,
            original_filename=file.name,
        )
        # Save file and generate preview
        file_path = data_upload.file.path
        try:
            if upload_type == 'excel':
                df = pd.read_excel(file_path)
            else:
                df = pd.read_csv(file_path)
            preview = df.head(10).to_dict(orient='records')
            data_upload.preview_data = preview
            data_upload.status = 'uploaded'
            data_upload.save()
        except Exception as e:
            data_upload.status = 'error'
            data_upload.error_report = str(e)
            data_upload.save()
        return redirect('upload_preview', upload_id=data_upload.id)
    return render(request, 'uploads/upload.html')

@login_required
def upload_preview(request, upload_id):
    data_upload = DataUpload.objects.get(id=upload_id)
    return render(request, 'uploads/preview.html', {'data_upload': data_upload})

@login_required
def map_columns(request, upload_id):
    data_upload = DataUpload.objects.get(id=upload_id)
    if request.method == 'POST':
        mapping = request.POST.get('mapping')
        data_upload.column_mapping = mapping
        data_upload.save()
        return redirect('validate_upload', upload_id=upload_id)
    return render(request, 'uploads/map_columns.html', {'data_upload': data_upload})

@login_required
def validate_upload(request, upload_id):
    data_upload = DataUpload.objects.get(id=upload_id)
    # Placeholder for validation logic
    errors = []
    # ... validation rules here ...
    if errors:
        data_upload.status = 'error'
        data_upload.error_report = '\n'.join(errors)
    else:
        data_upload.status = 'validated'
    data_upload.save()
    return render(request, 'uploads/validate.html', {'data_upload': data_upload, 'errors': errors})
