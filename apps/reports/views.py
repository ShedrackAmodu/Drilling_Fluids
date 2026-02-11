from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ReportTemplate, GeneratedReport
from .services import generate_pdf_report
from .tasks import generate_report_task

@login_required
def template_list(request):
    templates = ReportTemplate.objects.all()
    return render(request, 'reports/template_list.html', {'templates': templates})

@login_required
def generate_report(request, template_id):
    template = get_object_or_404(ReportTemplate, id=template_id)
    # create GeneratedReport and enqueue background task
    gen = GeneratedReport.objects.create(template=template, tenant=request.user.tenant_memberships.first().tenant, generated_by=request.user, parameters={})
    generate_report_task.delay(gen.id)
    return redirect('report_status', report_id=gen.id)
