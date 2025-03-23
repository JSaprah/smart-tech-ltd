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