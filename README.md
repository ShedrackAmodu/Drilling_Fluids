# DrillFlow

Minimal Django project skeleton for DrillFlow (drilling fluids platform).

Quick start (dev):

1. Create a Python 3.10+ virtualenv and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run migrations and start dev server:

```powershell
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

3. Admin: create superuser

```powershell
python manage.py createsuperuser
```

Files added: core models, admin registration, calculation service skeleton, docker-compose and env example.
