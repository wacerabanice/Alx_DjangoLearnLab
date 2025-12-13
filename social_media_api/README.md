Social Media API – Accounts Module

This project provides a custom user system built with Django and Django REST Framework (DRF). It supports user registration, login, and token-based authentication.

Setup
1. Clone the project
git clone <https://github.com/wacerabanice/Alx_DjangoLearnLab/tree/main/social_media_api>
cd social_media_api
2. Create and activate a virtual environment
python -m venv venv

Windows:

venv\\Scripts\\activate

Linux / macOS:

source venv/bin/activate
3. Install dependencies
pip install django djangorestframework pillow
4. Configure settings

In settings.py:

INSTALLED_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "accounts",
]


AUTH_USER_MODEL = "accounts.CustomUser"
5. Run migrations
python manage.py makemigrations
python manage.py migrate
6. Start the server
python manage.py runserver
Custom User Model

The project uses a custom user model that extends Django’s AbstractUser.

Additional fields:

bio – short user description

profile_picture – optional profile image

followers – self-referencing many-to-many relationship

Authentication

Token authentication is used.

Register
POST /api/accounts/register/
Login
POST /api/accounts/login/
Authenticated Requests

Include the token in headers:

Authorization: Token YOUR_TOKEN_HERE
Admin Access

Create an admin user:

python manage.py createsuperuser

Access the admin panel:

http://127.0.0.1:8000/admin/
