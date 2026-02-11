from django.core.exceptions import ValidationError

def validate_calculation_input(data):
    """Validate calculation input data (example: check required fields, value ranges, etc.)"""
    required = ['θ600', 'θ300']
    for field in required:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")
    # Add more validation as needed
    return True
