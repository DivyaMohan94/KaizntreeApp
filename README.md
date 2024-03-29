# Kaizntree App

# Hosted endpoints at http://18.217.166.192:8000/api/
# Postman requests and responses published @ https://documenter.getpostman.com/view/14658536/2sA2r3b6xw

# Technology Stack:
* Backend - Django
* Frontend - React
* Database - Amazon RDS(MySQL)
* Testing - Django APITestCase 
* Hosting - AWS
* Authentication & Permission - Django Token based authentication
* Testing - Postman

# Steps to Run backend:
* Ensure you have python3 and pip installed
* Clone the repository
* create a virtual environment using virtualenv venv
* Activate the virtual environment by running source venv/bin/activate
* Install the dependencies using pip install -r requirements.txt
* Migrate existing db tables by running python manage.py migrate
* Run the django development server using python manage.py runserver
* Test the end points using Postman
