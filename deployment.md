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

9. The prevent exposing the production database remove the PostgreSQL from the settings.

Set up hosting for our static and media files with AWS (Amazon Web Services). Specifically, we will use S3 (“Simple Storage Service”) for this.