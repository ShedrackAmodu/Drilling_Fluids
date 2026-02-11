#!/usr/bin/env python
<<<<<<< HEAD
"""Django's command-line utility for administrative tasks."""
=======
>>>>>>> 6d91a77d63a1f6db66d2efe8de474d92a5656fa0
import os
import sys


def main():
<<<<<<< HEAD
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drillflow.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise
>>>>>>> 6d91a77d63a1f6db66d2efe8de474d92a5656fa0
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
