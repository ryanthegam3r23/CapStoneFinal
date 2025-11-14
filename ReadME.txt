===========================================
 LiveSports Tracker - Django Web Application
===========================================

This project is a sports tracking web application built using Django.  
It provides live scores, sports news articles, user login/logout, and a clean,
responsive UI.

-------------------------------------------
 1. REQUIREMENTS
-------------------------------------------

Make sure you have the following installed:

- Python 3.10+
- pip (Python package manager)
- Virtual environment tool (optional but recommended)
- Git (optional)

Python packages (installed via requirements.txt):

- Django
- Requests (if live API calls are used)
- Pillow (if using images)
- Any other packages listed in requirements.txt


-------------------------------------------
 2. SETUP INSTRUCTIONS
-------------------------------------------

Follow these steps to run the project locally:

-------------------------------------------
 A) Create and Activate Virtual Environment
-------------------------------------------

On Windows:
    python -m venv venv
    venv\Scripts\activate

On Mac/Linux:
    python3 -m venv venv
    source venv/bin/activate

-------------------------------------------
 B) Install Dependencies
-------------------------------------------

Once the virtual environment is active:

    pip install -r requirements.txt

This installs all required Python packages.

-------------------------------------------
 C) Apply Database Migrations
-------------------------------------------

Run the following commands:

    python manage.py makemigrations
    python manage.py migrate

This sets up the database tables Django needs.

-------------------------------------------
 D) Create Admin User (Optional)
-------------------------------------------

To access Django's admin panel:

    python manage.py createsuperuser

Follow the prompts to create an admin account.

-------------------------------------------
 E) Run the Development Server
-------------------------------------------

Start the project using:

    python manage.py runserver

Then open your browser and go to:

    http://127.0.0.1:8000/

-------------------------------------------
 3. PROJECT STRUCTURE
-------------------------------------------

Important folders:

- /users/         : Login, logout, and registration system
- /pages/         : Static pages (home, about)
- /sportsnews/    : Sports news articles (list + detail pages)
- /live_scores/   : Live score tracking pages
- /templates/     : All HTML templates
- /static/        : CSS, images, and frontend assets
- /media/         : Uploaded media (if used)

Project root files:

- manage.py       : Main Django control script
- settings.py     : Django configuration
- urls.py         : Main URL routing
- requirements.txt: Python dependencies
- README.txt      : This file

-------------------------------------------
 4. USING THE APPLICATION
-------------------------------------------

Home Page:
    Displays project overview and navigation

News:
    Shows list of sports articles, each link opens a detail page

Scores:
    Displays live sports scores (if configured with an API)

User Accounts:
    Login and logout functionality included

Admin Panel:
    Visit /admin/ to manage content (requires superuser account)

-------------------------------------------
 5. TROUBLESHOOTING
-------------------------------------------

If the server fails to start:
    - Ensure the virtual environment is activated
    - Install dependencies again using:
          pip install -r requirements.txt

If templates or static files do not load:
    - Run:
          python manage.py collectstatic

If migrations are missing:
    - Run:
          python manage.py makemigrations
          python manage.py migrate


