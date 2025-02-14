# smart-tech-ltd

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

