# DrillFlow – No-Code Drilling Fluids Technology Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2+-green.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**DrillFlow** is a cloud-based, no-code, multi-tenant SaaS platform designed for drilling fluids engineering. It enables professionals to design, analyze, simulate, visualize, and report drilling fluids behavior without programming expertise, combining enterprise-grade capabilities with user-friendly workflows.

## 🎯 Vision

A cloud-based platform that replaces fragmented tools and spreadsheets with an integrated, standardized system for drilling fluids engineering—optimized for speed, visual clarity, and collaboration.

## ✨ Key Features

### 🚀 No-Code Engine
- Drag-and-drop workflow builder
- Visual configuration of rheology models, hydraulics, ECD, surge & swab
- Custom formula builder (UI-based)
- Workflow sequence: Data Input → Validation → Calculations → Charts → Reports

### 🛢️ Drilling Fluids Coverage
- Water-based mud (WBM), Oil-based mud (OBM), Synthetic-based mud (SBM)
- Completion & drill-in fluids
- Lab data analysis
- Mud design from scratch
- Excel/CSV upload support

### 📊 Calculations & Standards
- API RP 13B-1 / 13B-2 compliant calculations
- Hydraulics & hole cleaning
- ECD, surge & swab analysis
- Unit conversion (oilfield ↔ SI)
- Company-specific calculation overrides

### 📈 Visualization & Reporting
- Interactive charts & depth plots
- Rheology curves visualization
- Real-time monitoring dashboards
- Auto-generated PDF & Excel reports
- Company-branded template support

### 🔐 Multi-Tenancy & Security
- Company-isolated data architecture
- Role-based access control:
  - Admin (full access)
  - Engineer (create/edit)
  - Client (read-only)
  - Viewer (limited access)
- Secure API token authentication

### 🤖 AI-Assisted Intelligence (Future)
- Mud property recommendations
- Anomaly detection in fluid properties
- Parameter optimization suggestions
- "What-if" simulation scenarios

## 👥 Target Users

- **Mud Engineers** – Primary users for fluid design and analysis
- **Drilling Engineers** – Hydraulics and well planning
- **Supervisors & Operations Managers** – Monitoring and reporting
- **Consultants** – Client project work
- **Clients** – Read-only access for oversight
- **Academic/Training Users** – Future educational applications

## 🏗️ Technical Architecture

### Backend Stack
- **Language:** Python 3.10+
- **Framework:** Django (monolithic architecture)
- **API:** Django Rest Framework (internal APIs)
- **Database:** PostgreSQL with time-series optimization
- **Async Tasks:** Celery + Redis
- **ORM:** Django ORM

### Frontend Stack
- **Templating:** Django Templates (Server-side rendering)
- **Styling:** Bootstrap/Tailwind CSS
- **Interactivity:** HTMX/Alpine.js
- **Visualization:** Chart.js/Plotly
- **Offline Support:** Service Workers (future implementation)

### Deployment & Infrastructure
- **Development:** Local server environment
- **Containerization:** Dockerized services
- **Production:** DigitalOcean/Azure cloud hosting
- **Storage:** Object storage for files (future)
- **Bandwidth:** Optimized for low-bandwidth and offline scenarios

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- PostgreSQL database
- Redis server (for Celery)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/drillflow.git
   cd drillflow
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Django Admin: http://localhost:8000/admin/
   - Main Application: http://localhost:8000/

## 📁 Project Structure

```
drillflow/
├── config/                 # Django project configuration
│   ├── settings.py         # Application settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── apps/                   # Django applications
│   ├── users/             # User management
│   ├── wells/             # Well data management
│   ├── fluids/            # Fluid properties and samples
│   ├── calculations/      # Calculation engine
│   └── core/              # Core functionality
├── static/                # Static files
├── media/                 # User uploaded files
├── logs/                  # Application logs
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/drillflow

# Redis (for Celery)
REDIS_URL=redis://localhost:6379/1

# Email (for notifications)
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_TLS=True
```

### Static Files

For production, configure static files serving:

```python
# In settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### Media Files

Configure media file storage:

```python
# In settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run tests for a specific app:

```bash
python manage.py test apps.users
```

## 📊 Database Models

### Core Models

- **User**: Custom user model with company and role fields
- **Well**: Well information and metadata
- **WellSection**: Depth intervals and hole sizes
- **FluidType**: Fluid types (WBM, OBM, SBM)
- **FluidProperty**: Measurable properties (density, viscosity, etc.)
- **FluidSample**: Lab samples with measurements
- **FluidMeasurement**: Individual property measurements
- **Calculation**: Calculation results and parameters
- **Workflow**: No-code workflow definitions

## 🔐 Security

- Tenant-level data isolation
- Role-based access control (RBAC)
- Secure file upload validation
- Comprehensive audit logging
- API token authentication system
- Data encryption at rest and in transit

## 🚀 Deployment

### Docker

Build and run with Docker:

```bash
docker-compose up --build
```

### Production

1. Set `DEBUG=False` in production
2. Configure proper database and Redis connections
3. Set up static file serving (e.g., with Nginx)
4. Configure SSL/TLS certificates
5. Set up monitoring and logging

## 📈 API Documentation

The platform provides RESTful APIs for integration with external systems. API documentation is available at `/api/docs/` when the application is running.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:

- **Documentation**: [Link to documentation]
- **Issues**: [GitHub Issues](https://github.com/your-org/drillflow/issues)
- **Email**: support@drillflow.com

## 🙏 Acknowledgments

- API RP 13B-1/13B-2 standards compliance
- Django community for excellent framework
- Chart.js and Plotly for visualization libraries

---

**DrillFlow** – Modernizing Drilling Fluids Engineering Through Intelligent Automation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)