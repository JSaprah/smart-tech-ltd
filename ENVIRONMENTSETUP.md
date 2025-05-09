# smart-tech-ltd

This part covers the initial setup of the the workspace, the project, the allauth and the base template. The knowledge used for this part comes from the course content project boutique Ado.

## Setting up the workspace
The following steps where followed to setup a workspace for this project. The source used for this is: [Cheatsheet setting up a workspace](https://codeinstitute.s3.eu-west-1.amazonaws.com/PDF/Cheat+sheet_+Setting+up+a+workspace+in+VS+Code.pdf)

1. Create folder on my local machine in the 'vs-code-projects' folder
2. Open folder in VS Code IDE

In GitHub
3. In GitHub create a new repository
    - Start from no template
    - Keep the repository on public
    - Click on 'Create repository'
    - Copy the code for 'Create a repository from command line'

4. In VS Code open a new terminal and paste the copied command from the step above
5. A new Readme file appeared in the explorer sidebar as well as in GitHub. To test the connection I changed the text in the Readme file and pushed it to GitHub. This worked.

## Creating a virtual environment for Python

The following steps where followed to create a virtual environment. The source used for this is: [Cheatsheet Virtual Environment](https://codeinstitute.s3.eu-west-1.amazonaws.com/assets/venv/VEP_virtual-environments-cheat-sheet.pdf)

1. In your project on VS Code, open the command palette using the cog icon in the left bottom corner.
2. Type Create environment and select Python: Create environment
3. Select the Python version. In this project version 3.12.8 has been used.
4. Create file 'env.py' in VS Code. The Python version becomes visible in the bottom right side
5. Create a gitignore and add '.venv/' to and 'env.py' to this file. '/' is added so that it knows that it is a folder.

No issues were found following these steps.

## Install Django
1. Install Django with the command pip3 install django. For this project a lower version was used. The command used for this is pip3 install 'django<4'
2. Create project with command django-admin startproject smart_tech . (space dot at the end)
3. Add files to gitignore file 
    - *sqlite3: ignore database
    - *.pyc: ignore python compiled code
    - __pycache__: ignore compiled code
4. Run initial migration: python manage.py migrate to apply the changes
5. Run python manage.py runserver. Open the server. If this shows an error for disallowed host, add this to host name to the allowed host in the setting of the project. In this case, no error message was showing.

## Create superuser
1. To login as an Admin create a superuser: python manage.py createsuperuser. Provide username, email and password.
- Username: Jasmeen
- Email: j.sapraa@gmail.com
- Password: finalproject

## Allauth setup
1. Install allauth by using command: pip3 install django-allauth. To follow course content an older version has been installed pip3 install django-allauth==0.54.0
2. Go to the website [Allauth Authentication](https://docs.allauth.org/en/latest/installation/quickstart.html) and follow the instructions
    - Specify the cotext processor 'django.template.context_processors.request'. This is ussually in the settings already mention (for this project it was already there)
    - Add authentication backends.
    - Add app to installed apps
    - Add SITE_ID = 1 below the authentication backends
3. Add login urls to the urls.py file in the urlpatterns. This includes all the urls connected to allauth path('accounts/',include('allauth.urls'))
    - Import include from django.urls by adding include
4. Migration as new apps have been added with command python manage.py migrate
5. Open the /admin after running the server and login with the superuser credentials. Click on Sites and change the domain name and displayname. This is not a critical setting, but this would be in case of using social media authentication.

## Sending Emails
- By default Django sends confirmation emails to new accounts. We need to temporarily log those emails to the console so we can get confirmation links. To do so we can set the EMAIL_BACKEND setting to 'django.core.mail.backends.console.EmailBackend'
- Add additional settings below it (can be seen in settings.py file)

## Allauth templates
Allauth templates where retrieved by using these commands:
- pip3 show django-allauth
Copied the location from the above and pasted it in the command on the place of command
- cp -r <Location>/allauth/templates/* ./templates/allauth
- Deleted the openid and tests from allauth as I did not customize them

## Base template

1. Create a base.html file within the templates folder
2. Copy the starter template from Bootstrap documentation. This can be found in the introduction section of the documentation. [Starter template](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

In the head
1. Under required meta tags add '<meta http-equiv="X-UA-Compatible" content="ie=edge">'. This ensures that the older internet versions are supported and eliminates validation errors.
2. Delete the comments for cleanup.
3. Move the scripts from the body to the head to load them in in early phase. Replace the slim jquery version with the minified jquery version. The slim version does not include all the the features. Must be imported before popper and Bootstrap.
4. Add load static at the top for when we add static files later on.
5. Organise everything from base template in blocks. Which will give the ability to replace or extend the base template. 
6. For all parts also add an extra block. In case we want to add extra's without interferring the core requirements.

In the body
1. Add a header and a place to display messages
2. Add a block page header
3. Add a block content
4. Add a block postloadjs

## Create app
1. Create app home by python manage.py startapp home
2. Make a directory templates home by mkdir -p home/templates/home
3. Inside the templates/home directory create a html file called index.html
4. In the newly created template:
    - Extend base template
    - Load Static
    - Extend block content
5. Create a view to render the template in the file view.py
6. Create a new urls.py file in the home app
7. Copy the content of the urls.py file from the project to the home app
8. In this file; Import views, add a empty path, render views.index with a name of home
8. In the project urls.py file include the urls from the home app.
9. In the settings.py file of the project import os and add the base and the allauth templates in the dir: os.path.join(BASE_DIR, 'templates') and os.path.join(BASE_DIR, 'templates', 'allauth'),
10. Add the home app to the installed apps in the settings.py file of the project.

