## Bugs

The bugs identified during the project

1. 
    - Issue 1: When inserting a icon in my base file, this was not visible on my screen. I opened the console and I saw some error messages.  
    ![fontawesome error](fontawesomeerror.png)  
    
    - Solution: This issue got resolved by adding my personal fontawesome kit to the base file. 

2. 
    - Issue 2: CSS file not loading
    - Solution: I forgot to add the static files dir to the settings. Adding this to the setting solved the error 404 not found.

3. Adding the shopping bag was causing the error of url not found. The reason for this was that I added '/bag' to the urls.py file of the bag app and also added this to the project urls.py file. This caused the error that the browser was looking for a url /bag/bag which it could not find. After removing /bag from the urls.py bag app the issue got resolved.

4. Upon clicking on the substraction and addition button in the product detail page the shopping bag was being updated. Solution: Adding the preventDefault function solved prevented that the data was automatically send to the backend


5. While updating the product quantity in the bag and clicking on the save button the quantity would not be saved. I requested tutor support for this issue. Walking through this issue and adding some print statements, it appeared that the the function was recognising the button as an object instead of the form. Changing the function .prev to .closest helped solving this issue. 

6. Submitting the checkout form was causing the issue: fadeToggle() is not a function. After debugging it appeared that I was using a Jquery version that did not want to take this as a function. I changed it from minified version to the slim version. This solved the issue. 

7. After resolving the previous issue I encountered a follow up issue; The form was now being submitted and the data was send to Stripe. However, the response was being returned as none instead of HTTPResponse. After debugging I saw that I was missing a field - last name in mt view. After adding the view my issue got resolved.

8. Remove function in the bag was not working. Having a look at it it appeared that I added the remove in the type instead of the the class. Therefore the function was not being triggered.

9. In my shopping bag upon updating the quantity, input fields for all product would change. To solve this I requested tutor support. Looking at the walkthrough project, the support team advised me to make use of the function closest to only interact with the product. This solution worked out for me. 

10. Creating the wishlist model I created only one class for the wishlist. I worked on the feature adding the product to the wishlist. This worked all really well, untill I decided to work on the remove from wishlist function. I discovered, instead of adding the products to the wishlist, it was creating every time a new wishlist with a unique combination. I did some research and understood that I have to create two classes; One for the wishlist and one for the items with a relation between them. Upon changing the model, I came across many errors. It had some data save in my wishlist model, therefore it was not able take my changes. I deleted the older migration files and tried to do the rework, but it did not work. I had a talk with tutor support and with the following approach, I managed to delete all items in the wislist table. 
 - Run command: python manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude wishlist > db.json
 - Rename file db.sqlite3 to db.backup.sqlite3.
 - Run command: python manage.py migrate
 - Run command: python manage.py loaddata new.json
 
 This made sure that I had a backup before making changes as the the db.backup.sqlite3 file contains the previous data, with the broken wishlist data, your new dbs.qlite3 file contains all of your old data except for the wishlist data.


 11. Heroku deployment failed with the reason that there is no static root in the settings. By adding the static root in the settings the deployment went succesfull with all static and media files loaded.

 12. Deployment to Production via Heroku. I followed all deployment steps carefully and my site was configured correctly. With One issue that the bag was not loading in Production - I got a server error 500. Unfortunatelly, I was not able to see what exactly was going wrong, there I was advice to put the Debug to True and make a deployment to identify and solve the issues. After putting the debuug to True, it apeared that a the quantity_input_script.html template was not working correctly. The issue was that I used backslashes in the url instead of /. Changing this and deploying it back to production solved the issue. 
