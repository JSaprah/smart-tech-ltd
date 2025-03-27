## Creating the PostgreSQL with Code Institute

This is created with Code Institute as the Heroku add-ons are not available on the Student Pack.

1. Navigate PostgreSQL from Code Institute: [PostgreSQL](https://dbs.ci-dbs.net/)
2. Enter email and receive the database URL

A new instance of database has been created


## 2.Create an app on Heroku for hosting

1. Login into Heroku: [Heroku](https://dashboard.heroku.com/apps)
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

For this part the instruction on this document were followed [Creating an AWS](https://codeinstitute.s3.eu-west-1.amazonaws.com/fullstack/Creating-an-AWS-+account.pdf)

1. Go to [Amazon AWS](https://aws.amazon.com/)
2. Create an AWS account

### Step 1: Create a bucket
1. Enter a bucket name
2. Select ‘ACLs enabled’
3. Select ‘Bucket owner preferred’
4. Deselect ‘Block all public access’
5. Check the box to acknowledge the risk of public access
6. Leave the other options unchanged and click ‘create bucket’

### Step 2- Enable static website hosting

When the bucket is created, click on the bucket name to view the bucket details. Click on the ‘Properties’ tab. Scroll down to the ‘static website hosting’ section and click ‘Edit’
1. Click ‘Enable’
2. Enter ‘index.html’ (without quotes) into the Index document input
3. Enter ‘error.html’ (without quotes) into the Error document input
4. Click ‘Save changes’


### Step 3- Change CORS configuration
 
 Click on the permissions tab.  Scroll down to the Cross-origin resource sharing (CORS) section and click ‘Edit'.
1. Add the following code for the CORS settings
2. Click ‘Save changes’
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

### Step 4- Add a bucket policy

 On the Permissions tab of your S3 bucket, scroll to the ‘Bucket policy’ section and click ‘Edit’.  Click ‘Policy Generator'.  This will open in a new tab. 

 1. For the policy type you can select ‘S3 Bucket Policy’
 2. For the principal you can enter “*” without quotes
 3. For the Action select ‘GetObject’ from the dropdown

  Then go back to the bucket policy editor in the other tab and click this button to copy the ARN.

  Then go back to the Policy Generator in the other tab
 1. Paste the ARN into the ARN input
 2. Click ‘Add Statement’

 Scroll down and click ‘Generate Policy’.  Copy all of the text in the popup.
 1. Go back to the policy editor in the other tab and paste in the policy code
 2.  Edit the ‘Resource’ value by adding /* to the end, to allow access to all objects within the bucket
 3. Save changes


 ### Step 5- Edit the Access Control List (ACL)

  On the ‘Edit Access control list’ page:
 1. Click ‘List’ in the Everyone (public access)
 2. Click the checkbox to indicate that you understand the effects of the change
 3. Click ‘Save changes'


 ## Creating AWS Groups, Policies and Users
 
 These instructions were followed to create AWS Groups Policies and users. [Creating AWS Groups Policies and users](https://codeinstitute.s3.eu-west-1.amazonaws.com/fullstack/Creating-AWS-Groups-Policies-and-Users.pdf)

 ### Step 1- Create a user group

 1. Search for ‘iam’ in the search bar at the top
 2. Click on ‘IAM’
 3. Click ‘User Groups’ on the left. Click ‘Create Group’.  Enter a group name. I have used 89566b21efa9-smart-tech-ltd.
 4. Scroll down to the bottom and click ‘Create user group’.

### Step 2- Create a policy

  Click ‘Policies’ in the menu to the left. 
  1. Click the ‘JSON’ tab
  2. Click the ‘Actions’ dropdown
  3. Click ‘Import policy’
  - Search for ‘s3’
  - Select ‘AmazonS3FullAccess’
  - Click ‘Import Policy’
  
  1. Search for ‘s3’ at the top
  2. Right click ‘S3’
  3. Click ‘Open in a new tab’

  In the new tab:
 1. Select your bucket
 2. Click ‘Copy ARN’

Go back to the previous tab and add your ARN in quotes to the ‘Resource’ list twice, for the
 second one add /* after the ARN.

 Scroll to the bottom and click ‘Next’.  Enter a policy name and description.  Scroll down and click ‘Create policy’. 


### Step 3- Attach the policy to the group

Click ‘User groups’ in the menu to the left:
 1. Click the ‘Permissions’ tab
 2. Click the ‘Add permissions’ dropdown
 3. Click ‘Attach policies’


 1. Search for your policy (you can search for the policy name or description that you
 entered previously)
 2. Select the checkbox beside your policy
 3. Click ‘Attach policies’


### Step 4- Create a User

1. Click ‘Users’ in the menu to the left
2. Click ‘Create user’
3. Enter an user name and click next. I have added smart-tech-user
4. Scroll down and click ‘Create user’


###  Step 5- Create an Access Key
1. Click on your new user:
2. Click ‘Security credentials’
3. Scroll down to the ‘Access keys’ section and click ‘Create access key’
4. Select ‘Application running outside AWS’
5. Click ‘Next’
6. Click ‘Create access key’
7. Scroll down and click ‘Download .csv file’
8. Click ‘Done’
9. Open the .csv file in any text editor (such as Notepad on Windows, TextEdit on Mac). 
This will contain the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to use as a config var in Heroku

## Connecting Django to S3

### Step 1 - Install packages
1. Boto3: pip3 install boto3
2. Django storages: pip3 install django-storages
3. Freeze requirements: pip3 freeze > requirements.txt

### Step 2 - Update django settings
1. Add storages to the installed apps in the settings
2. Add condition in the settings to use AWS

if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = '89566b21efa9-smart-tech-ltd'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'


With AWS_S3_CUSTOM_DOMAIN We tell django where our static files will be coming from in production. Which is going to be our bucket name. .s3.amazonaws.com

### Step 3 - Add config vars in Heroku

1. Add AWS_ACCESS_KEY_ID copied from the Amazon AWS
2. Add AWS_SECRET_ACCESS_KEY copied from the Amazon AWS
3. Add a variable for USE_AWS and set the value to True. So that our settings file knows to use the AWS configuration when we deploy to Heroku.
4. Remove DISABLE_COLLECTSTATIC. Since the deployment should now take the media files and store it automatically to S3 bucket.

### Step 4 - Create file custom storages in the root

The next step is to tell django that in production we want to use s3 to store our static files whenever someone runs collectstatic. And that we want any uploaded product images to go there also.

1. Create file custom_storages in django
2. Add two classes: StaticStorage and MediaStorage. In both classes pass the location
3. Go back to settings Tell it that for static file storage we want to use our storage class we just created. And that the location it should save static files is a folder called static. And then do the same thing for media files by using the default file storage.
And media files location settings. We also need to override and explicitly set the URLs for static and media files. Using our custom domain and the new locations.

What happens now is when our project is deployed to Heroku. Heroku will run python3 manage.py collectstatic during the build process.
Which will search through all our apps and project folders looking for static files.And it will use the s3 custom domain setting here
in conjunction with our custom storage classes that tell it the location at that URL.Where we'd like to save things.
So in effect when the USE_AWS setting is true. Whenever collectstatic is run. Static files will be collected into a static folder in our s3 bucket. The beauty of this is that it's all automatic.