"""
Question : Why Django should be used for web-development? Explain how you can create a project in Django?
Answer : 
-> Rapid Development: Django's ready-to-use components let developers build applications quickly.
-> Scalability: Suitable for handling high traffic and heavy data loads.
-> Built-in Admin Interface: Provides an auto-generated admin panel, which saves time.
-> Security: Offers protection against SQL injection, XSS, CSRF, and clickjacking.
-> Versatile Framework: Works well for both small and large projects.
-> ORM (Object-Relational Mapping): Simplifies database interactions.
-> REST Framework Support: Easily builds APIs with Django REST framework.
-> Large Community & Documentation: Strong community support and extensive documentation.
-> Reusability: Reusable code and app modules for faster development.


Steps to create a Django Project : 
1. pip install python
2. pip install django
3. django-admin startproject <projectname>
4. cd <projectname>
5. python manage.py startapp <appname>
6. Go to settings.py and add the app in the INSTALLED_APPS section.
7. python manage.py migrate
8. python manage.py runserver

Visit `http://127.0.0.1:8000/` to see the default Django page.

"""
