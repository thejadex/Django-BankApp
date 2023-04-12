# BankApp
<h1> Django Bank App </h1>

Django Bank App is a web-based banking application built using Django framework. This app allows users to manage their accounts, transfer funds to other accounts, view transaction history(coming soon).

<h1> Requirements </h1>
    <ul>Python 3.6 or higher</ul>
    <ul>Django</ul>
    <ul>PostgreSQL</ul>
  
<h1> Getting Started </h1>
  <h3>Installation</h3>
      <p>Clone this repository to your local machine</p>
      <li>git clone https://github.com/TheJadeX/BankApp <br></li>
      <hr>

Install the required packages using pip
<li>pip install -r requirements.txt <br></li>
<hr>

<p>Set up the PostgreSQL Database</p>
<li>Create a new PostgreSQL database with a name of your choice. </li> <br>
<li>Edit the DATABASES configuration in Bank App/settings.py to match your PostgreSQL configuration.</li> <br>

      '''DATABASES = { 
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your-db-name',
        'USER': 'your-db-username',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': '5432',
        }
      }'''
    
<hr>

<p>Apply the database migrations</p>

<li>python manage.py migrate</li> <hr>
        
<p>Create a superuser account.</p>

<li>python manage.py createsuperuser</li> <hr>

<p>Run the development server</p>
<li> python manage.py runserver</li> <br>
<p>The application should now be available at http://localhost:8000.</p> <hr>

<h1>Usage</h1>
    <ol>
        <li>To access the admin panel, navigate to http://localhost:8000/admin and log in with the superuser account credentials.</li>
        <li>To view the user-facing application, navigate to http://localhost:8000/.</li>
        <li>Use the application to manage accounts, transfer funds, view transaction history, and more.</li>
    </ol> <hr>

<h1>License</h1>
    <p>Django Bank App is licensed under the MIT license. See LICENSE for more information.</p>
  
