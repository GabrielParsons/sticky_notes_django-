# Sticky Notes Django Application

A simple Django web application for creating, viewing, editing, and deleting sticky notes with author assignment capabilities.

## Features

- Create sticky notes with title and content
- Assign authors to sticky notes
- View all sticky notes in a visually appealing sticky note style
- Edit existing sticky notes
- Delete sticky notes
- Admin panel for managing notes and authors
- Comprehensive documentation with Sphinx
- Docker support for easy deployment

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Methods](#installation-methods)
  - [Method 1: Using Virtual Environment (venv)](#method-1-using-virtual-environment-venv)
  - [Method 2: Using Docker](#method-2-using-docker)
- [Environment Variables](#environment-variables)
- [Documentation](#documentation)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Prerequisites

### For Virtual Environment Setup:
- Python 3.9 or higher
- pip (Python package installer)

### For Docker Setup:
- Docker installed on your system
- Docker Compose (optional, for advanced setups)

## Installation Methods

### Method 1: Using Virtual Environment (venv)

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd sticky_notes
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv myenv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables (optional but recommended for production):**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and set your Django secret key:
     ```bash
     # Generate a new secret key:
     python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
     ```
   - Add the generated key to your `.env` file

6. **Navigate to the Django project directory:**
   ```bash
   cd sticky_notes
   ```

7. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

8. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up your admin username, email, and password.

9. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

10. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

11. **Access the application:**
    - Main app: http://127.0.0.1:8000/
    - Admin panel: http://127.0.0.1:8000/admin/

12. **To deactivate the virtual environment when done:**
    ```bash
    deactivate
    ```

### Method 2: Using Docker

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd sticky_notes
   ```

2. **Set up environment variables (recommended):**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Generate a new Django secret key:
     ```bash
     python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
     ```
   - Update the `.env` file with your secret key and other settings

3. **Build the Docker image:**
   ```bash
   docker build -t sticky-notes-app .
   ```

4. **Run the container:**
   ```bash
   docker run -p 8000:8000 sticky-notes-app
   ```
   
   Or with environment variables from your `.env` file:
   ```bash
   docker run -p 8000:8000 --env-file .env sticky-notes-app
   ```

5. **Access the application:**
   - Main app: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

6. **To create a superuser in Docker:**
   ```bash
   # First, find your running container ID
   docker ps
   
   # Then execute the createsuperuser command
   docker exec -it <container-id> python manage.py createsuperuser
   ```

7. **To stop the container:**
   ```bash
   docker stop <container-id>
   ```

### Testing on Docker Playground

You can also test this application on [Docker Playground](https://labs.play-with-docker.com/):

1. Create a new instance
2. Clone the repository
3. Build and run the Docker container as described above
4. Click on the port badge (8000) that appears to access the application

## Environment Variables

The application supports the following environment variables for configuration:

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `DJANGO_SECRET_KEY` | Secret key for Django (CHANGE IN PRODUCTION!) | Development key (insecure) |
| `DJANGO_DEBUG` | Enable/disable debug mode | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `*` (all hosts) |

**⚠️ IMPORTANT SECURITY NOTES:**

- **Never commit your `.env` file or any files containing secrets to version control**
- The `.gitignore` file is configured to exclude `.env` files
- Always generate a new secret key for production deployments
- Set `DJANGO_DEBUG=False` in production environments
- Configure `DJANGO_ALLOWED_HOSTS` to only include your domain(s) in production

### Generating a Secure Secret Key

To generate a new Django secret key:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy the output and use it as your `DJANGO_SECRET_KEY` in the `.env` file.

## Documentation

This project includes comprehensive documentation generated with Sphinx.

### Viewing the Documentation

1. **Navigate to the documentation directory:**
   ```bash
   cd docs/_build
   ```

2. **Open `index.html` in your web browser:**
   - On macOS: `open index.html`
   - On Linux: `xdg-open index.html`
   - On Windows: `start index.html`

### Rebuilding Documentation

If you make changes to the docstrings and want to rebuild the documentation:

1. **Activate your virtual environment** (if using venv)

2. **Install Sphinx dependencies** (if not already installed):
   ```bash
   pip install sphinx sphinx-rtd-theme
   ```

3. **Navigate to the docs directory:**
   ```bash
   cd docs
   ```

4. **Build the documentation:**
   ```bash
   sphinx-build -b html . _build
   ```

## Project Structure

```
sticky_notes/
├── .dockerignore              # Files to exclude from Docker builds
├── .env.example              # Example environment variables file
├── .gitignore                # Git ignore patterns
├── dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── docs/                     # Sphinx documentation
│   ├── conf.py              # Sphinx configuration
│   ├── index.rst            # Documentation index
│   ├── modules/             # Module-specific docs
│   └── _build/              # Generated HTML documentation
│
└── sticky_notes/            # Django project root
    ├── manage.py            # Django management script
    │
    ├── sticky_notes/        # Project settings
    │   ├── settings.py     # Django settings (with env var support)
    │   ├── urls.py         # Root URL configuration
    │   ├── asgi.py         # ASGI configuration
    │   └── wsgi.py         # WSGI configuration
    │
    └── stickynotes/         # Main application
        ├── models.py        # StickyNote and Author models
        ├── views.py         # CRUD views with docstrings
        ├── forms.py         # StickyNoteForm with docstrings
        ├── urls.py          # App URL patterns
        ├── admin.py         # Admin interface configuration
        ├── apps.py          # App configuration
        ├── tests.py         # Tests
        │
        ├── migrations/      # Database migrations
        │   └── 0001_initial.py
        │
        ├── static/          # Static files (CSS)
        │   └── stickynotes/
        │       └── styles.css
        │
        └── templates/       # HTML templates
            ├── base.html
            └── stickynotes/
                ├── stickynotes_list.html
                ├── stickynotes_detail.html
                └── stickynotes_form.html
```

## Technologies Used

- **Backend:** Django 4.2.27
- **Frontend:** Bootstrap 5.3.8 (via CDN)
- **Database:** SQLite (default, can be configured for PostgreSQL, MySQL, etc.)
- **Documentation:** Sphinx with Read the Docs theme
- **Containerization:** Docker
- **Python Version:** 3.9+

## Development Notes

- The `myenv/` folder (virtual environment) is excluded from version control
- The `db.sqlite3` database file is excluded from version control
- Static files are collected during Docker build and deployment
- The application uses Django's built-in development server (not suitable for production)

## Admin Panel

To access the admin panel and manage notes and authors:

1. Navigate to http://127.0.0.1:8000/admin/ (or http://localhost:8000/admin/ for Docker)
2. Log in with the superuser credentials you created
3. You can add, edit, and delete sticky notes and authors from the admin interface

## Troubleshooting

### Virtual Environment Issues

- **Command not found:** Make sure you've activated the virtual environment
- **Permission denied:** On Unix systems, you may need to make manage.py executable: `chmod +x manage.py`

### Docker Issues

- **Port already in use:** Change the port mapping: `docker run -p 8080:8000 sticky-notes-app`
- **Build fails:** Ensure Docker is running and you have sufficient disk space
- **Container exits immediately:** Check logs with `docker logs <container-id>`

### Database Issues

- **Migration errors:** Try deleting `db.sqlite3` and running migrations again
- **Permission errors:** Ensure the Django process has write permissions to the database directory

## Contributing

This is a learning project. Feel free to fork and experiment!

## License

This project is for educational purposes.

## Author

Gabe Parsons

