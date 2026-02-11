from celery import shared_task
from .models import GeneratedReport
from .services import generate_pdf_report

@shared_task
def generate_report_task(generated_report_id):
    gen = GeneratedReport.objects.get(id=generated_report_id)
    file_content = generate_pdf_report(gen.template, gen.parameters)
    gen.file.save(file_content.name, file_content)
    gen.status = 'completed'
    gen.save()
