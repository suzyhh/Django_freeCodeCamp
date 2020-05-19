## This is the freeCodeCamp Django for Beginners tutorial on YouTube
## www.youtube.com/watch?v=F5mRW0jo-U4&t=10872s
## https://github.com/codingforentrepreneurs/Try-Django


cd /Users/suzy/Documents/STP/Django_freeCodeCamp
# Make a virtual env
python3.7 -mvenv cfenv
# Activate env
source cfenv/bin/activate
# Upgrade pip
pip install --upgrade pip
# Install Django 
pip install -r requirements.txt
# Create Django project
mkdir src
cd src
django-admin startproject trydjango .
# Test the server 
python manage.py runserver
# Navigate to http://127.0.0.1:8000

# Set up git repository
git init
git config --global user.name "suzyhh"
git config --global user.email suzyhocking@gmail.com

# This shows info about untracked/modified/staged files, branch status etc
git status

# Tracks all files in working directory
git add --all

# Commit (save) the changes
git commit -m "Initial commit"
# I created the repository in GitHub first
git remote add origin https://github.com/suzyhh/Django_freeCodeCamp
git push -u origin master

# Sync database with django project
# Syncs with DATABASES = {} in settings.py
 python manage.py migrate

# Creat superuser to accesss the admin app on http://127.0.0.1:8000/admin
# This user is stored in the database. It's all a databse.
python manage.py createsuperuser
# Username (leave blank to use 'suzy'): suzy_cfe
# Email address: 
# Password: Jelly101
# Password (again): Jelly101
# Superuser created successfully.

# Make a custom app called 'products'
# Each app should do one thing only, and do it well. It has a narrow focus
python manage.py startapp products

# Now go into products/models.py and build a model for products
# Run both of these whenever you make changes to models.py
# This detects and makes changes
python manage.py makemigrations
python manage.py migrate

# Don;t forget to register your models in admin.py

# Create new Product objects in python, rather than on the website
python manage.py shell
>>> from products.models import Product
>>> Product.objects.all()
    <QuerySet [<Product: Product object (1)>]>
# Make a new product
>>> Product.objects.create(title="new product 2", description="another",price="999",summary="sweet")
>>> Product.objects.all()
    <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>


# Adding new model fields
# Delete everything but init.py in migrations, and also the sqlite database
# Make some changes to Products in models.py
python manage.py makemigrations
python manage.py migrate

# And as we deleted the database, re-creat superuser
python manage.py createsuperuser
# Username (leave blank to use 'suzy'): suzy_cfe
# Email address: 
# Password: Jelly101
# Password (again): Jelly101
# Superuser created successfully.

# You can make a change to the models without deleting the migrations and database
# So if you add a field to a model, the database doesnt know it's there, i.e. what about all the previous objects in the database that dont have any data for that field?
# That's what the default thing does
# or you can add null=True, which allows the field in previous objects to be blank
# It checks against what's in 0001_initial.py
# If you try to make migration with a new field and choose option 1, you can pick a default. This makes a new 0002_product_featured.py


##### URL #####
# Think of views.py as the doc that handles web pages


# Make a new app called pages and add it into settings.py own apps
python manage.py startapp pages
# So make the homepage view by opening /pages/views.py, make sure its the correct app folder!
# Import the view you just made into urls.py