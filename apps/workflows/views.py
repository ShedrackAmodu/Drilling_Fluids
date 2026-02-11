from django.shortcuts import render, get_object_or_404
from .models import Workflow

def workflow_list(request):
    workflows = Workflow.objects.all()
    return render(request, 'workflows/list.html', {'workflows': workflows})

def workflow_detail(request, workflow_id):
    wf = get_object_or_404(Workflow, id=workflow_id)
    return render(request, 'workflows/detail.html', {'workflow': wf})
