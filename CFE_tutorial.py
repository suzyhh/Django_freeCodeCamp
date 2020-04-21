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

 