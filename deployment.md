## Creating the PostgreSQL with Code Institute

This is created with Code Institute as the Heroku add-ons are not available on the Student Pack.

1. Navigate PostgreSQL from Code Institute: https://dbs.ci-dbs.net/
2. Enter email and receive the database URL

A new instance of database has been created


## 2.Create an app on Heroku for hosting

1. Login into Heroku: https://dashboard.heroku.com/apps
2. Click on create app
- Provide a unique app name - smart-tech-ltd
- Chose the closest region - Europe
- Click on create app. A new app will be created

3. Open the settings app
- Add the config var DATABASE_ URL
- Add the url of the database (without quotes) as the value 


## Connect database to the local development web server

With the above steps a database instance has been created and an Heroku app is configured, the database can be connected to the local development web server. The steps followed to do so are mentioned below:

1. In the terminal, install dj_database_url and psycopg2 with the command: pip3 install dj_database_url==0.5.0 psycopg2
2. Update requirements.txt with command: pip freeze > requirements.txt
3. In the settings import dj_database_url underneath the os
4. Scroll to DATABASES and comment out the original connection instead connect to the new database. Paste the database URL from PostgreSQL from Code Institute. Do not commit this file with the production database as this is only for migrating the data to the new database. 
5. In the terminal run the command: python manage.py showmigrations to confirm you are connected to the external database
6. Migrate your database models to your new database with command: python manage.py migrate
7. Load the fixtures. The order is very important
- First load the categories: python manage.py loaddata categories
- Then products: python manage.py loaddata products
8. Create superuser with command: python3 manage.py createsuperuser
- Follow the instructions by providing a user name, password and email (email is not mandatory).
9. This prevent exposing the production database remove the PostgreSQL from the settings.


## Deploying to Heroku

### Hiding the secret key

1. In the env.py file add: 'os.environ.setdefault('SECRET_KEY', 'Your secret key here')'
2. In settings.py file: change the secret key to SECRET_KEY = os.environ.get('SECRET_KEY')' instead of hard-coding.
3. import os at the top of the env.py file.
4. import env at the top of the settings.py file.


### Preparing the work for deployment
1. In settings.py locate DATABASES and update the code conditional based so that it can automatically correspond to the correct database by:

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

2. Make the env file conditional

if os.path.isfile('env.py')
    import env

3. Create Procfile in the root directory
- In this file we will tell Heroku to create a web dyno and run gunicorn to serve our Django app: "web: gunicorn smart-tech-ltd.wsgi:application"

4. To ensure that Heroku uses the correct version of Python to work with all the project's dependencies, add a runtime.txt file to the root directory. Inside it, add the following line of code: python-3.11.11

5. In Heroku open the app and copy the url of the app

6. In settings.py, add the URL for your app to the ALLOWED_HOSTS. Important: Remove https:// from the start of the URL, and the trailing slash from the end of the URL.

### Installing gunicorn - deployment

1. In the terminal install gunicorn: pip3 install gunicorn
2. Freeze requirements: pip3 freeze --local > requirements.txt
3. Save, commit and push all your changes to GitHub.


### Preparing Heroku settings for deployment

1. In your Heroku application, navigate to the app settings.
2. Open the Config Vars.
3. Create a new environment variable called DISABLE_COLLECTSTATIC, and give it a value of 1.
For our initial deployment, we need to temporarily disable Heroku from collecting static files from our project. This step prevents Heroku from uploading static files, such as CSS and JS, during the build. In a future topic, we'll set up an AWS account to manage these files. For now, the DISABLE_COLLECTSTATIC environment variable will prevent deployment errors, allowing us to successfully deploy our site without accessing static files.
4. Create a new environment variable called SECRET_KEY, and set its value to a random string. Your Heroku secret key should not be the same as the one set in your env.py file. You can use a service such as https://randomkeygen.com/ to generate secret keys.

### Deploying the app
1. On your Heroku app dashboard, select the Deploy tab.
2. Here, we will connect our Heroku app to our GitHub repository and deploy our project. Scroll to the Deployment method and select GitHub
3. Search for your repository name, then click Connect
4. Click the Enable Automatic Deploys button. This will ensure that any time you push new code to your GitHub repository, Heroku will deploy the updated application.
5. Click Deploy Branch to deploy your project.
6. Heroku should build the app now. Once completed the app should be accesible via its url/ open app button.


### Conditionally setup DEBUG

1. Once you confirm that your project has deployed—albeit without the static files connected—we'll conditionally set DEBUG to True only in the development environment.

Important: Setting DEBUG to True leaves your site vulnerable to security issues. Therefore, it must be set to False when deployed.
In settings.py, update the DEBUG value to True only if an environment variable named DEVELOPMENT is present.

DEBUG = 'DEVELOPMENT' in os.environ


2. In env.py, add a new environment variable for DEVELOPMENT and set it to '1'

os.environ.setdefault('DEVELOPMENT', '1')
Then, commit and push your changes to GitHub.
Note: Your product images will no longer show on Heroku now that DEBUG is set to False. Don't worry; in the next lesson, we'll host them with AWS.

3. If there are any add-ons you can check and remove it via the resources tab. In my case there where no add-ons.

## Set up hosting for our static and media files with AWS (Amazon Web Services). Specifically, we will use S3 (“Simple Storage Service”) for this.