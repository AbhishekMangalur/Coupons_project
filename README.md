# Coupon Distribution System

## **1. Install Required Software**
Before starting, make sure you have the following installed:
- ✅ **Python (3.8 or later)** – [Download from python.org](https://www.python.org/downloads/)
- ✅ **Django (4.x recommended)** – Python web framework
- ✅ **MySQL** – Database
- ✅ **A web server (for deployment)** – [PythonAnywhere](https://www.pythonanywhere.com/)

---

## **2. Install Dependencies**
Run the following commands to install the required dependencies:
```sh
pip install python
pip install django
pip install mysqlclient
```

---

## **3. Create and Run the Project**
Use the following commands to set up and run the project:

### **Create the Project & App**
```sh
django-admin startproject coupon_project   # Creating the Django project
cd coupon_project
django-admin startapp coupon_app           # Creating the app
```

### **Set Up Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv     # Creating a virtual environment
source venv/bin/activate  # (Linux/Mac) Activate virtual environment
venv\Scripts\activate    # (Windows) Activate virtual environment
```

### **Apply Migrations**
```sh
python manage.py makemigrations   # Creating migrations
python manage.py migrate          # Creating tables in the database
```

### **Run the Server**
```sh
python manage.py runserver  # Runs the project
```

Your project will be accessible at: **http://127.0.0.1:8000/**

---

## **4. Additional Commands**
### **Create Superuser (For Admin Panel)**
```sh
python manage.py createsuperuser  # Follow the prompts to create an admin user
```

### **Deploy to PythonAnywhere**
1. Sign up at **[PythonAnywhere](https://www.pythonanywhere.com/)**
2. Upload your project files
3. Configure your **web app** in the PythonAnywhere dashboard
4. Run the following commands:
```sh
python manage.py migrate
python manage.py runserver
```
5. Your project will be live on **PythonAnywhere**!

---

## **5. Reset Database (If Needed)**
To clear all coupon claims and reset the database, run:
```sh
python manage.py shell
```
```python
from coupon_app.models import CouponClaim, Coupon
CouponClaim.objects.all().delete()
Coupon.objects.update(is_claimed=False)
print("Coupons reset successfully!")
```

---

## **6. Next Steps**
✅ **Test your project**
✅ **Deploy it online**
✅ **Enhance with additional features (Admin Dashboard, Email Notifications, etc.)**

Now your **Coupon System** is fully functional & ready for deployment! 🚀🔥

