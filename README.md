1. Install Required Software
Before starting, make sure you have:
✅ Python (3.8 or later) – Download from python.org
✅ Django (4.x recommended) – Python web framework
✅ MySQL – Database
✅ A web server (for deployment) – PythonAnywhere

2. Required commands for the install Dependencies
pip install python
pip install django
pip install mysqlclient

3. Commands for create and run the project
django-admin startproject coupon_project	          # creating a project
django-admin startapp coupon_app	                  # creating app
python -m venv venv	                                # creating virtual environment
python manage.py makemigrations		                  # creating migraions
python manage.py migrate	                          # creating tables in database
python manage.py runserver	                        # runs the project
