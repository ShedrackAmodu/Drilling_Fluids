import io
from django.core.files.base import ContentFile

# Placeholder services for report generation (PDF/Excel) - integrate with reportlab/xlsxwriter later

def generate_pdf_report(template, parameters):
    # For now create a simple text-based PDF placeholder (real implementation: reportlab)
    content = f"Report from template: {template.name}\nParameters: {parameters}\n"
    return ContentFile(content.encode('utf-8'), name=f"report_{template.id}.pdf")

def generate_excel_report(template, parameters):
    # Placeholder - integrate with xlsxwriter or openpyxl
    content = f"Excel report placeholder for {template.name}\n"
    return ContentFile(content.encode('utf-8'), name=f"report_{template.id}.xlsx")
