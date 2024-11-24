Install Python

Download the latest version from python.org/downloads.
Ensure to check the box "Add Python to PATH" during installation.
Clone the Repository

bash
Copy code
git clone https://github.com/ITEC660/homework-7-nelson.koranteng
cd homework-7-nelson.koranteng
Set Up Virtual Environment

bash
Copy code
pip install virtualenv
virtualenv env
Activate the Virtual Environment:
Windows:
bash
Copy code
cd env/Scripts
activate
cd ../..
macOS:
bash
Copy code
source env/bin/activate
You will see (env) in your prompt, indicating the virtual environment is activated.
Setting Up Django
Install Django

Copy code
pip install django
Check Installed Packages

Copy code
pip freeze
Create a Django Project

Copy code
django-admin startproject myproject
A myproject directory will be created with the default Django structure.

Run the Server

bash
Copy code
cd myproject
python manage.py runserver
Visit http://localhost:8000/ to verify that the Django project was successfully created.

Building the App
Create an App

Copy code
django-admin startapp mycontactsapp
A mycontactsapp directory will be created.

Define a View

Open mycontactsapp/views.py and edit:
python
Copy code
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')
Configure URLs

Edit myproject/urls.py:
python
Copy code
from django.contrib import admin
from django.urls import path
from mycontactsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
Run the Server
Visit http://localhost:8000/ to see "Hello, world".

Adding a Contact Model
Define the Model

Edit mycontactsapp/models.py:
python
Copy code
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
Register the App

Add 'mycontactsapp' to INSTALLED_APPS in myproject/settings.py.
Apply Migrations

Copy code
python manage.py makemigrations mycontactsapp
python manage.py migrate
Create a Superuser

Copy code
python manage.py createsuperuser
Access the Admin Panel

Run the server:
Copy code
python manage.py runserver
Visit http://localhost:8000/admin/, log in, and add some contacts.
Displaying Contacts
Update Views

Edit mycontactsapp/views.py:
python
Copy code
from django.http import HttpResponse
from .models import Contact

def index(request):
    mylist = ""
    for i in Contact.objects.all().order_by('first_name'):
        mylist += f"{i.first_name} {i.last_name}<br>"

    return HttpResponse(f"<div style='text-align:center; font-size:20px;'>All Contacts:<br>{mylist}</div>")
Visit http://localhost:8000/
You will see all contacts listed alphabetically, centered, and styled with CSS.

