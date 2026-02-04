# Sticky Notes Django Application

A simple Django web application for creating, viewing, editing, and deleting sticky notes.

## Features

- Create sticky notes with title and content
- Assign authors to sticky notes
- View all sticky notes in a visually appealing sticky note style
- Edit existing sticky notes
- Delete sticky notes
- Admin panel for managing notes and authors

## Installation

1. **Clone the repository or extract the files**

2. **Create a virtual environment:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the project directory:**
   ```bash
   cd sticky_notes
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the application:**
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
sticky_notes/
├── manage.py
├── sticky_notes/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── stickynotes/          # App
    ├── models.py         # StickyNote and Author models
    ├── views.py          # CRUD views
    ├── forms.py          # StickyNoteForm
    ├── urls.py           # URL patterns
    ├── admin.py          # Admin registration
    ├── templates/        # HTML templates
    │   ├── base.html
    │   └── stickynotes/
    │       ├── stickynotes_list.html
    │       ├── stickynotes_detail.html
    │       └── stickynotes_form.html
    └── static/           # CSS files
        └── stickynotes/
            └── styles.css
```

## Technologies Used

- Django 4.2.27
- Bootstrap 5.3.8 (via CDN)
- SQLite (default database)

## Note

The `myenv/` folder (virtual environment) is excluded from version control and should not be submitted. Generate it locally using the installation instructions above.
