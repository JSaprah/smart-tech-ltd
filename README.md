# smart-tech-ltd

Smart Tech is a fictional B2C electronics store crafted with Django, Python, HTML, and CSS. It serves as a sleek, modern platform for showcasing the newest and trendiest tech products. From must-have gadgets to innovative accessories, Smart Tech lets users explore it all effortlessly. Shoppers can browse the full collection or filter items by category. With a robust search function and a built-in stock management system, customers can shop with confidence.

Once signed in, customers can save their delivery address for a faster checkout process. They can also revisit their order history, making it simple to keep track of previous purchases.

This project was inspired by a love for cutting-edge technology and the dream of creating an online store that connects people with the latest innovations. While that dream evolved, Smart Tech became a showcase project and a valuable tool for learning and mastering Django and Python development.

The deployed site can be visited here: [Smart Tech](https://smart-tech-ltd-89566b21efa9.herokuapp.com/)


![Smart_Tech](docs/responsiveness.png)

## Project Planning

### Site aims
Electronics have become an integral part of everyday life, offering convenience, entertainment, and innovation to consumers. From sleek gadgets to cutting-edge components, the range of products is vast and ever-evolving. For some, staying up-to-date with the latest tech is a necessity; for others, it’s a passion or even a lifestyle. In any case, the demand for reliable and high-quality electronics continues to grow.

Smart Tech aims to be the online face of a fictional electronics store, providing a simple yet sophisticated interface for customers to browse and shop for the newest tech products and accessories. It is designed with the user in mind, ensuring a seamless and enjoyable shopping experience.

This site serves as the virtual storefront for a fictional electronics shop, enabling customers to easily explore and purchase a curated range of products. The site is built to showcase all items in one place while offering robust search and filtering options to help users find exactly what they need.

For this project, the focus is on categories that any modern tech store would feature. While some stores specialize in niche markets like gaming accessories or smart home devices, Smart Tech’s approach is to offer a wide variety of essential tech products that cater to a broad audience.


### Core Product Categories

The minimum product categories essential for a tech store of this nature include:

* Audio Equipment: Headphones, earphones, and portable speakers.
* Accessories: Chargers, cables, and protective gear for devices.
* Gaming Gear: Controllers, keyboards, and gaming headsets.

This selection ensures that Smart Tech appeals to both tech enthusiasts and casual shoppers, providing everything needed to stay connected, productive, and entertained.

For the future this site can be extended with products, such as:

* Smartphones: The latest models with cutting-edge features.
* Laptops: Ranging from lightweight ultrabooks to high-performance gaming rigs.
* Smart Home Devices: Assistants, security cameras, and automation systems.
* Wearable Technology: Smartwatches, fitness trackers, and health monitors.


### Scope
Given the timeline for this project and the required grade criteria, trade-offs in design and development will be necessary. Using the agile methodology, I will track the progress and adjust, add, or remove features as needed. This iterative process will ensure that a Minimum Viable Product (MVP) is delivered by the deadline.

To avoid scope creep, the MoSCoW method has been used to prioritize and categorize features. This approach will help maintain focus and achieve the goal of delivering a fully functional MVP.

#### Must-Have Features

To ensure the MVP meets essential requirements, the following features will be implemented:

* Full CRUD (Create, Read, Update, Delete) functionality.
* User login/register system.
* Seamless checkout system.
* User account profile management.
* Mailing list subscription.
* Product sorting and searching capabilities.
* Integration with Stripe for payments.
* SEO-friendly language throughout the site.
* Guest checkout option.
* User role permissions.
* Order history for users.
* Social media page integration.
* Login in, registering and password recovery.
* Email confirmation for orders.
* User feedback for actions taken (toasts).
* Saved customer details during checkout.


#### Should-Have Features
These features elevate the customer experience:

* Product Reviews: Shoppers can rate and leave opinions.
* Stock management interface for product management.
* Contact Form: Facilitates user queries.
* Wishlist Feature: Allow users to save favorite items for future consideration.


#### Could-Have Features

Exploring these additions can attract and engage customers:

* Tech Insights Blog: Content that educates and excites.
* Product Demos: Videos showcasing key features.
* Related Recommendations: Suggest complementary items.
* Order Modifications: Editable orders until processing begins.
* Terms & Conditions: Clear policies for transparency.
* Delivery Information: Accessible details about shipping options.
* Coupon code for extra discount
* Special Offers


#### Will Not Address

Certain features are excluded from scope:

* Currency Options: Support for multiple currencies.
* Third-Party Reviews: Trustpilot integration.
* Advanced Analytics: Sales report generation.


### Structure

To create a well-organized and efficient e-commerce platform, I designed a class diagram that establishes the relationships between key components of Smart Tech. The backbone of this structure is Django's built-in User class, extended with a UserProfile model using a OneToOneField relationship to enhance customization and user management.

In addition to the core models, three custom models (from the should have methodology) have been introduced during the project to enrich the functionality of the platform:

* Wishlist: Allows users to save and manage their favorite products for future consideration.
* Reviews: Enables customers to leave ratings and feedback on purchased products, fostering engagement and trust.
* Contact: Provides a streamlined way for customers to submit inquiries or feedback, improving communication between the store and its users.

Other primary models include:

* Product: Defines product details such as name, category, price, stock status, and descriptions.
* Checkout: Manages the checkout process, linking orders to users and handling essential transactional details.

This diagram lays the foundation for a cohesive, scalable system where each component integrates seamlessly to deliver a polished shopping experience. While Agile development allows for flexibility and iterative improvements, this diagram ensures the system's core structure remains robust and aligned with project goals.

![class diagram Smart Tech](docs/flowcharts/diagram_smart_tech.PNG)


### User Stories

To support the AGILE development process, I have crafted a comprehensive set of user stories. These stories serve as a roadmap to help prioritize the features and functionalities required for the site. They are instrumental in ensuring the successful delivery of a Minimum Viable Product (MVP) within the project deadline. The user stories are grouped into milestones (also on GitHub) for better organization and focus. After each sprint, these stories will be reviewed and updated as part of the iterative process, ensuring continuous alignment with project goals.


#### Milestone 1: Viewing and Navigating

|User Story ID| As an| I want to be able to| So that|
|-------------|------|---------------------|--------|
|1.|Shopper|Browse a selection of products|I can make a purchase|
|2.|Shopper|See the details of each product|I can chose the right one to buy|
|3.|Shopper|I want to see the total price in my basket at all times|I can monitor my spending|
|4.|Shopper|Save items to a wishlist|I can revisit and purchase them later|
|5.|Shopper|Contact the store effortlessly|I can ask questions or seek assistance when needed|


#### Milestone 2: Registering and accessing account

|User Story ID| As an| I want to be able to| So that|
|-------------|------|---------------------|--------|
|1.|Site User|Effortlessly sign up for an account|I can have a personal profile|
|2.|Site User|Conveniently log in or log out|I can access personal account information|
|3.|Site User|Login and logout option|Access my personal account details and securely logout|
|4.|Site User|Recover my password if I forget|I can regain access to the account|
|5.|Site User|Have a personalised user profile|I can view my order history, order cofirmations and save payment information|


#### Milestone 3: Filtering and sorting

|User Story ID| As an| I want to be able to| So that|
|-------------|------|---------------------|--------|
|1.|Shopper|Easily see search results and the number of results|I can quickly decide if the desired product is available|
|2.|Shopper|Search for products by name or description|I can find specific items to buy|
|3.|Shopper|Sort the list of available products|I can identify the best rates, prices, and categories|


#### Milestone 4: Purchasing and checkout

|User Story ID| As an| I want to be able to| So that|
|-------------|------|---------------------|--------|
|1.|Shopper|Easily select the quantity of a product when purchasing|I can buy the required amount of the product|
|2.|Shopper|view items in the shopping bag|identify the total cost and all items to be received|
|3.|Shopper|Modify the quantity of items in my shopping bag|I can effortlessly make adjustments before purchasing.|
|4.|Shopper|Receive an email summary of my order after checking out|I can maintain a record for future reference|
|5.|Shopper|Review my order history|I can track previous purchases at a glance|
|6.|Shopper|Submit my payment details securely|I get the guarantee the safety of my financial data|


#### Milestone 5: Adminstering and Managing products

|User Story ID| As an| I want to be able to| So that|
|-------------|------|---------------------|--------|
|1.|Store Owner|Add new products to the store effortlessly|I can ensure the catalog stays fresh and relevant|
|2.|Store Owner|Modify existing product details|the information stays up-to-date|
|3.|Store Owner|Delete outdated or unavailable product|I can keep the store inventory organized and accurate|


#### Milestone 6: Product reviews
|User Story ID| As an| I want to be able to| So that|
|-------------|------|---------------------|--------|
|1.|Shopper|Leave a review|I can share my experience for a product|
|2.|Shopper|Read reviews from other customers|I can understand the quality and value of a product|
|3.|Shopper|remove my previously submitted reviews|I can take down feedback that I no longer wish to display|


### Skeleton
Wireframes were crafted to bring the vision of Smart Tech to life. These wireframes provided a visual guide for the site's layout and functionality, offering clarity during the initial planning phase. While the wireframes served as an essential foundation, some adjustments were made during development to accommodate time constraints and practical considerations.

The wireframes were created for both mobile view and desktop view ensuring responsiveness.

The wireframes include:

#### Home Page

Designed for a welcoming first impression with clear navigation.

![Home page wireframes](docs/wireframes/wireframe_home.PNG)  


#### Products Page

Focused on showcasing items with intuitive filtering and sorting.

![Product page wireframes](docs/wireframes/wireframe_products.PNG)  


#### Product Details Page

Highlighting essential product information to aid decision-making.

![Product details page wireframes](docs/wireframes/wireframe_product_details.PNG)  


#### Add/edit product page
Add/Edit Product Page: Provides the store owner with a dedicated page to efficiently update the product catalog, ensuring inventory accuracy and relevance.

![Add/edit page wireframes](docs/wireframes/wireframe_product_add_edit.PNG)


#### Shopping bag Page

Ensuring users can easily review and edit their selections.

![Shopping bag page wireframes](docs/wireframes/wireframe_bag.PNG)


#### Checkout Page

Streamlined for quick and hassle-free payment.

![Checkout page wireframes](docs/wireframes/wireframe_checkout.PNG)  


#### Order Confirmation Page

This page provides a clear confirmation that their order has been successfully processed. 

![Order confirmation page wireframes](docs/wireframes/wireframe_order_confirmation.PNG)  


#### User Profile Page

Providing access to user details and order history.

![User Profile page wireframes](docs/wireframes/wireframe_profile.PNG)  

#### Wishlist Page: 

Allows users to save items of interest for later, encouraging thoughtful and repeat purchases.

![Wishlist page wireframes](docs/wireframes/wireframe_wishlist.PNG)

#### Contact Page: 

A simple, user-friendly form for inquiries or feedback, ensuring smooth communication with store administrators.

![Contact page wireframes](docs/wireframes/wireframe_contact.PNG)  

These visualizations guided the site's structure while ensuring alignment with user needs and project goals.

When creating the wireframes the sorting dropdown was not taken into consideration. This is an addition for all the product screens.


## Agile Development process

I have used GitHub to manage my agile process, dividing user stories into six focused milestones to ensure a clear workflow and prioritize essential functionality. 

Each milestone addresses a specific aspect of the user experience:

1. Viewing and Navigating: This milestone focused on creating a seamless browsing experience, including intuitive navigation, responsive design, and easy access to all product categories. Users can efficiently explore the store and locate desired items.

2. Registering and Accessing Account: This milestone ensured users could register, log in, and manage their accounts securely. Features like password reset and email verification were implemented to optimize accessibility and data protection.

3. Purchasing and Checkout: Concentrated on building the shopping cart functionality and ensuring users could complete their purchases effortlessly. Secure payment gateways and a streamlined checkout process were key elements in this milestone.

4. Filtering and Sorting: Developed advanced filtering and sorting options to enhance the user experience. Users can quickly narrow down search results based on price, categories, or other criteria to find exactly what they need.

5. Administrating and Managing Products: Focused on backend functionality for administrators, including the ability to add, edit, and delete products. This milestone streamlined product management to ensure the catalog remained up-to-date.

6. Product Reviews: Implemented a robust review system, allowing users to add, edit, and delete reviews. This feature fosters community engagement and helps other customers make informed decisions.

These milestones helped break the development process into manageable segments, ensuring each feature met its objectives efficiently.

![Agile Milestones](docs/Agile_milestones.PNG)  


## E-commerce application type

As previously described, Smart Tech is a B2C e-commerce platform built to cater directly to individual consumers. The website is strategically designed to facilitate quick, seamless shopping experiences, ensuring customers can browse, select, and purchase their desired tech products efficiently. The primary focus is on user convenience and satisfaction, with functionality tailored for simple navigation, detailed product exploration, and a smooth checkout process.

While scaling to wholesale or B2B sales might be a future consideration, the current version of Smart Tech emphasizes selling innovative and cutting-edge gadgets, accessories, and gaming products in smaller quantities. This approach allows the site to remain user-centric, meeting the needs of tech enthusiasts who seek a personalized and streamlined shopping journey.

### SEO

For the keywords I tried using [Wordtracker](wordtracker.com) and other tooling. Unfortunatelly, there was some kind of subscription on it. I decided to go with my own ideas and I made a brain dump of more general keywords and product specific the short tail and the long tail keywords.

General keywords

|Tech related|Ecommerce|
|------------|---------|
|Must-have tech gadgets|Online marketplace|
|Latest tech gear|Ecommerce platforms|
|Compact smart devices|Fast shipping|
|Unique wearable tech|Buy online now|
|Innovative gadgets for home|Personalised shopping experience|
|Trending gadgets|Online shopping deals|


Headsets

|Short-tail|Long-tail|
|-------------|------|
|Wireless headphones|Best buy wireless headphones for sports|
|Noise-cancelling headsets|Bluetooth in-ear headphones with noise cancellation|
|Gaming headsets|Surround sound gaming headsets for competitive play|


Charging Cables

|Short-tail|Long-tail|
|-------------|------|
|USB-C charging cables|Universal magnetic charging cables for multi-device use|
|Fast charging cables|Braided USB-C cables with fast charging capabilities|
|Lightning cables|Durable iPhone lightning cables for daily use|

Gaming

|Short-tail|Long-tail|
|-------------|------|
|Gaming consoles|Exclusive multiplayer gaming|
|gaming accessories|Best games for family-friendly fun|
|Virtual reality gaming|Trending games to play at home|


### Marketing strategies

To increase visibility, foster engagement, and drive sales the following strategies haven been implemented:

* Mailchimp Newsletters: Subscription to the mailing list to send tailored content to different customer groups (e.g., gamers, tech enthusiasts). Currently, it is possible to signup. No emails are being send.

![Mailchimp](docs/Marketing/mailchimp.png)  

* Customer reviews highligted on the product details page. Positive reviews can build trust and influence new customers.This can be extended with actively requesting for reviews and testimonials and showcasing them on the website as well as the Facebook page. This feature has been added to the website on product level for the product details page. You can read more about it in the section below.


* Facebook business page: Helps with connecting to customers, building brand awareness, and driving engagement. It is designed to complement the e-commerce store by offering a platform for updates, promotions, and customer interaction.

A Facebook business page is created with a profile image, cover image, call to action, my first post. [Facebook link to the page](https://www.facebook.com/profile.php?viewas=100000686899395&id=61575026153772) can be found here.

A printscreen has been added in case of deactivation:  

![Facebook business page](docs/Marketing/facebook.png)  


A further exansion of marketing can be done by:

* Sharing product showcases and polls to engage with followers. This fosters interaction and keeps the brand visible in customers feeds.
* Facebook Ads: Use targeted paid advertisements to reach tech enthusiasts, gamers, and gadget lovers based on demographics and interests.
* Include tech tips, trending product recommendations, and early access to sales to keep readers engaged
* Start a Tech Blog on the website to share insights, how-to guides, and tech trends. Optimize articles with keywords to boost traffic through search engines. Include product-focused content such as unboxing videos, tutorials, or comparison reviews, which can be shared on Facebook and newsletters.
* Partner with relevant tech bloggers and YouTubers who can promote Smart Tech products in exchange for a commission on sales.
* Provide affiliates with promotional materials like discount codes or custom links to make it easy for them to market your products.
* Set up Google Shopping Ads to showcase Smart Tech products directly in search results. These ads allow potential customers to see the product image, name, price, and brand, increasing conversion rates for those searching for specific items.
* Referral Program: Incentivize customers to refer friends and family to Smart Tech by offering discounts or rewards for successful referrals. Promote the referral program prominently on the website, Facebook page, and newsletters.
* Social Media Expansion: Extend the brands social media presence to other platforms like Instagram and TikTok. Create engaging short-form videos showcasing products, tech tips, or gaming setups.
* Launch seasonal campaigns, such as back-to-school tech bundles, holiday sales, or gaming tournaments with special prizes. Use Facebook and newsletters to promote these events.


## Features

### Page content

#### Home page

At the heart of the Home Page is a sleek and minimal introduction that captures the essence of the brand. This pages provides a simple call to Action: A prominently placed button labeled “Shop now" invites users to dive right into exploring the product catalog effortlessly.

![Home page desktop](docs/features/desktop/home_page_desktop.PNG)  
![Home page mobile](docs/features/mobile/home_page_mobile.PNG)  

#### Product Page

The Products Page is designed to provide users with an effortless browsing experience to explore the store’s offerings. It combines a sleek layout with functionality to ensure that shoppers can quickly find and sort products tailored to their needs. It mainly covers the user stories for sorting, filtering and viewing all products.

* Search Results Display: Shoppers can easily view search results with the total number of matching items clearly indicated.
* Search Functionality: Responsive search bar allows users to locate products by entering keywords related to the name or description
*Sorting Options: Shoppers can sort results using filters by name, category and price.

![Product page desktop](docs/features/desktop/products_page_desktop.PNG)  
![Product page mobile](docs/features/mobile/products_page_mobile.PNG)  


#### Product Management CRUD functionality for Admins

The add, edit and delete functionality is a feature for store administrators to manage the product catalog. This is designed with simplicity and efficiency in mind, allowing admins to quickly add new products, update the details of an existing product or delete the product.

Key features

##### Add Product

Accesible via the top menu dropdown for profile. Only admins can see this option.

* Admins are presented with a clean, easy-to-use form to input all necessary product details:
    * Product Name
    * Description
    * Price
    * Category (Headsets, Gaming, Accessories)
    * Image Upload

![Add Product page desktop](docs/features/desktop/add_product_desktop.PNG)  
![Add Product page mobile](docs/features/mobile/add_product_mobile.PNG)  


##### Edit Product

Accesible via the product details page with the button edit product. Only admin can see this button.

Pre-Populated Fields:
* When editing a product, the form is pre-populated with the current details of the selected product.
* This allows admins to quickly identify and adjust the information they wish to modify, such as updating the price or changing the description.

Validation:
Each field is validated to ensure proper formatting, such as requiring non-empty fields and numeric values for price and stock. The form ensures that all updates meet the same validation standards as adding a new product, avoiding incomplete or incorrect entries.

![Edit Product page desktop](docs/features/desktop/edit_product_desktop.PNG)  
![Edit Product page mobile](docs/features/mobile/edit_product_mobile.PNG)  


##### Delete Product

Button in the product details page only visible for the admins to delete the button.

caution: Currently there is no modal around it to confirm the deletion of the product. Upon clicking the button the product will directly be deleted.

#### Product Details Page

The Product Details Page is designed to provide shoppers with all the information they need to make informed purchasing decisions. This page includes four key sections to streamline the user experience:

* Product Overview: Displays the product's name, price, a detailed description, and an image. Shoppers can select a quantity for purchase directly from this section.

* Reviews: Features a dedicated tab where users can:
    * Read existing reviews to gain insights from other customers.
    * Leave their own review and assign a star rating to share their experiences with the product.
    * For authenticated users, options to delete previously submitted reviews are included, allowing opinions removed as needed.

![Product details page reviews](docs/features/components/product_details_page_reviews.PNG)  
![Product details page reviews desktop ](docs/features/desktop/product_details_page_reviews_desktop.PNG)  
![Product details page reviews mobile ](docs/features/mobile/product_details_page_reviews_mobile.PNG)  

* Wishlist Integration: A heart icon enables users to instantly add the product to their wishlist with a single click, making it easy to save items for future consideration.

* Admin Controls: Superusers are empowered to:
    * Edit product details directly from this page, such as descriptions, pricing, or stock status.
    * Remove products from the store inventory that are no longer available for sale.


![Product details page desktop](docs/features/desktop/product_details_page_desktop.PNG)  
![Product details page mobile](docs/features/mobile/product_details_page_mobile.PNG)  

#### Shopping bag Page

The Shopping Bag Page acts as a crucial checkpoint in the customers shopping journey, allowing them to review and manage their selections before proceeding to checkout. 

Key Features and Functionalities:

* Overview of Items:
    * Displays all items added to the shopping bag, with essential details such as product name, price, quantity, and a thumbnail image.
    * Provides a subtotal for each item to ensure customers can see how much each product contributes to the total cost.

* Quantity Adjustment:
    * Users can easily modify the quantity of any product using the plus and minus sign.
    * Once changes are made, an update Button allows the cart to refresh with the new totals. This ensures a hassle-free method for adjusting purchases.

* Item Removal:
    * A Remove Button is included for each item, allowing users to delete unwanted products directly from the shopping bag.

* Bag Summary:
    * Total cost, including subtotals.
    * Delivery charges, if applicable.

* Call to action
    * A Continue Shopping Button enables users to return to browsing without losing their current selections.
    * A Proceed to Checkout Button redirects users to finalize their purchase.

* Empty Bag Notification:
    * If a user accesses the page with no items in the bag, a friendly message informs them that their shopping bag is empty, with suggestions to start shopping or explore featured categories.


![Shopping bag page desktop](docs/features/desktop/shopping_bag_page_desktop.PNG)  
![Shopping bag page mobile](docs/features/mobile/shopping_bag_page_mobile.PNG)  


#### Checkout page

The checkout page provides users with a seamless and secure shopping experience. Key features include:

* Product Summary: Displays the products added to the cart along with the subtotal.
* Add and Save Details: Users have the option to enter and save their billing and shipping information for convenience.
* Integrated Payment System: Card payments are powered by Stripe, ensuring reliable and efficient transactions.
* Security: Stripe integration ensures high-level security, safeguarding user data throughout the checkout process.

![Checkout page desktop](docs/features/desktop/checkout_page_desktop.PNG)  
![Checkout page mobile](docs/features/mobile/checkout_page_mobile.PNG)  

![Confirmation email](docs/features/components/confirmation_email_order.png)  

#### Order confirmation page

The Order Confirmation Page serves as the final step in the shopping journey, ensuring customers feel assured and informed after placing an order. This page provides a clear confirmation that their order has been successfully processed. Key details displayed include:

* A confirmation message thanking the customer for their purchase.
* The order number for easy reference
* A summary of the purchased items, including quantities and prices.
* Additionally, users will receive an email confirmation with these details, providing a record of their transaction for future reference.

![Order confirmation page desktop](docs/features/desktop/order_confirmation_desktop.PNG)  
![Order confirmation page mobile](docs/features/mobile/order_confirmation_mobile.PNG)  

#### User profile page

The User Profile Page is designed to provide customers with a personalized space where they can manage their account details and track their order history.

Key Features:

Account Overview:
* Displays the user’s delivery address

Editable Personal Information:
* Users can update their saved details for delivery address
* A simple form allows users to make changes, ensuring their data is always accurate and up-to-date.


Order History:
Provides a list of all previous orders, including details like:

* Order date
* Order number
* Items purchased
* Total cost

Each order entry includes a View Details button that redirects users to the Order Confirmation Page for a more detailed summary of the transaction.

Wishlist:
If the user has saved items to their wishlist, they can view it from the wishlist - heart icon on the top.


![Profile page desktop](docs/features/desktop/profile_page_desktop.PNG)  
![Profile page mobile](docs/features/mobile/profile_page_mobile.PNG)  


#### Wishlist Page

The Wishlist functionality is designed to enhance the shopping experience by allowing users to save products for future consideration. It bridges the gap between browsing and purchasing, giving users the flexibility to revisit items they’re interested in. Here's how it works:

Adding Items to the Wishlist:
From the Product Details Page, users can click the heart icon to add the product to their wishlist. This one-click action ensures that users can effortlessly save items without disrupting their browsing flow.

Managing the Wishlist:
Users can access their wishlist via the dedicated Wishlist Page, which displays all saved items in a clean and organized layout.
* Each item is presented with key details, such as product name, image, price, and availability.

Product Actions in the Wishlist:
* Delete: Users can remove items they no longer wish to save directly from the wishlist, maintaining control over their saved collection.
* View Details: Clicking on a product redirects users back to the Product Details Page, where they can review the item’s full description and make a purchase decision.

Personalization:
The wishlist is tied to each users account, ensuring that saved items are accessible across sessions for logged-in users.


![Wishlist page desktop](docs/features/desktop/wishlist_page_desktop.PNG)  
![Wishlist page mobile](docs/features/mobile/wishlist_page_mobile.PNG)  

### Contact page

The Contact Page is designed to facilitate seamless communication between users and the store’s support team. It prioritizes simplicity and accessibility, allowing customers to submit inquiries, feedback, or any concerns effortlessly.

It consists of a user-friendly form; includes fields for:
* Name
* Email Address
* Subject
* Message

![Contact page desktop](docs/features/desktop/contact_page_desktop.PNG)  
![Contact page mobile](docs/features/mobile/contact_page_mobile.PNG)  


### Common to all pages

#### Header

The Header Component is designed to provide users with a seamless navigation experience and quick access to essential features, ensuring a smooth and intuitive interaction with the website. Its features are carefully structured to enhance usability and responsiveness.

Features Overview:

* Company Logo: The logo is prominently displayed and serves as a clickable link that redirects users to the Home Page. This ensures users can quickly return to the homepage from any section of the site.

* Navigation Elements: The header includes a navigation menu with links to:
* All Products: Displays the full product catalog.
* Gaming: Redirects users to a dedicated section for gaming-related products.
* Accessories: Includes subcategories for specific items like:
    * Headsets
    * Charging Devices

* Contact: Directs users to the Contact Page for inquiries and feedback.

Top Menu:

* My Account: A dropdown menu with options to:
    * Login/Logout: Users can authenticate or end their session.
    * Profile: Access the users profile page to manage account details and view order history.

* Super User Options: For administrators, an additional option for Product Management is displayed in the dropdown to add products to the catalogue.

* Wishlist: Enables users to view and manage products saved for later consideration.

* Bag: Shows the shopping basket total, allowing quick access to the shopping bag.

* Search Bar: Allows users to search for specific products by name or description. On smaller screens, the Search Bar is hidden for optimized space usage.A toggle logo in the top menu lets users hide/unhide the Search Bar, ensuring accessibility on all devices.

![Header desktop](docs/features/components/header_desktop.PNG)  
![Header mobile](docs/features/components/header_mobile.PNG)  

#### Footer

The Footer Component is a simple yet effective section designed to enhance user engagement and ensure easy access to essential resources and updates. It is structured to provide key features:

* Facebook Integration: Includes a link to the company's official Facebook page, allowing users to stay connected and updated with the latest news, offers, and announcements.


* Mailchimp Subscription Form: A Mailchimp-powered newsletter subscription form enables users to sign up for monthly updates.
Subscribers gain access to exclusive offers, discount codes, and the latest product news. The form ensures accessibility with required fields marked by an asterisk (*), clearly guiding users during signup. For the MVP no real communication is being send out. It is only possible to signup.

* Copyright Information: Displays a copyright notice, attributing the project to its creator and clearly stating its educational purpose. Ensures transparency by declaring that no commercial revenue is generated from the project.

![Footer desktop](docs/features/components/footer_desktop.PNG)  
![Footer mobile](docs/features/components/footer_mobile.PNG)  


#### Authentication

Django's build in Authentication System is designed to securely manage user access and ensure a seamless experience for customers. This functionality includes:

##### Login
Allows registered users to log in using their email address and password. Ensures secure authentication with hashed passwords and encrypted data transmission. After successful login, users gain access to personalized features such as their account profile and wishlist.

![Login](docs/features/components/login.PNG)

##### Logout
Provides users with a clear option to log out from the website via the My Account dropdown menu. Upon logout, the session data is cleared, ensuring that no sensitive information is retained.

![Logout](docs/features/components/logout.PNG)

##### Register
Enables new users to create an account by submitting their email address and personal details via a registration form. Sends real-time emails using the configured email server to verify the users email address upon registration.
Ensures secure password creation and validation to protect user accounts. Additionaly, it creates a profile for the user.

![Register](docs/features/components/register.PNG)

##### Password Reset
Allows users to reset their password via a "Forgot Password?" link on the login page. Generates a secure, time-limited password reset link and sends it to the user's registered email address.

![Password reset](docs/features/components/password_reset.PNG)

The authentication system ensures a robust and user-friendly experience while prioritizing security and ease of use.


#### Toasts 
Toast messages are present throughout the site to give users feedback on the actions they performed. These are divided in error, success, alert and information.

Examples of toast can be seen below:  

![alert toast](docs/features/components/toasts/alert.png)  
![success toast](docs/features/components/toasts/success.png)  


#### 404 Page
A custom 404 page is present to keep the experience personalised. 

![404 error desktop](docs/features/components/404_error.png)   

## Future features

While the current version of Smart Tech delivers a functional and engaging user experience, there are several exciting features planned for future development to enhance its usability, scalability, and appeal:

* Option for Coupon Codes for Discounts. A coupon code system will allow users to apply discounts during checkout, encouraging repeat purchases and rewarding customer loyalty. Admins will be able to create and manage coupon codes via the admin panel, including options for expiration dates and minimum spend requirements.

* Delivery Details and Tracking Information: Enhancements to delivery functionality will include estimated delivery times displayed during checkout and order confirmation. Additionally, users will have access to tracking information for their packages, ensuring transparency and convenience throughout the shipping process.

* Advanced Stock Management To streamline operations, a robust stock management system will be implemented. This system will:
    * Display the quantity of items in stock on the product page.
    * Restrict purchases exceeding available stock levels.
    * Automatically reduce stock levels when products are sold, keeping inventory accurate. The automation of stock management will reduce manual input and prevent overselling, improving efficiency and reliability.

* More Images per Product: Products will feature multiple images to provide users with a comprehensive view of each item, enhancing the shopping experience. Admins will be able to upload multiple images per product, including dynamic views, close-ups, or lifestyle shots, to ensure customers can make informed decisions.

Other features that have not been implemented from the MoSCoW method and could implemented in the future:
* Currency Options: Support for multiple currencies.
* Third-Party Reviews: Trustpilot integration.
* Advanced Analytics: Sales report generation.
* Tech Insights Blog: Content that educates and excites.
* Product Demos: Videos showcasing key features.
* Related Recommendations: Suggest complementary items.
* Order Modifications: Editable orders until processing begins.
* Terms & Conditions: Clear policies for transparency.
* Delivery Information: Accessible details about shipping options.
* Coupon code for extra discount

Other features that have been excluded due to time constraints
* Option to edit reviews
* Options for the admins to be notified when being contact and replying on them/ adding notes to them
* Special Offers

## Testing and bug fixes

I have included testing details during and post-development in a separate document called [TESTING.md](TESTING.md)

## Deployment

The final Deployed site can be found [here](https://smart-tech-ltd-89566b21efa9.herokuapp.com/) I have included details of my initial deployment in a separate document called
[DEPLOYMENT.md](deployment.md)


## Technologies

The Smart Tech project leverages a range of technologies and tools to build, style, deploy, and manage the e-commerce platform effectively. Below is an overview of the technologies used:

* Backend and Frameworks
    * Python: The core programming language used for backend logic and functionality.
    * All installed packages are listed in the requirements.txt file for easy dependency management

* Django: A powerful Python web framework used to develop the core functionality of the website.

* Database: 
    * SQLite: Utilized as the database during the development phase to test models and features locally.
    * PostgreSQL: Used for database management in the deployed application to ensure scalability and reliability.

* Frontend Technologies
    * HTML: Forms the backbone for structuring and templating the website pages.
    * CSS: Custom CSS is implemented for styling, ensuring a unique and visually appealing design.
    * Bootstrap: A front-end framework used for styling and layout consistency. It simplified the creation of responsive designs.
    * Font Awesome: Integrated for icons throughout the site to improve visual appeal and navigation.

* Frontend Interactivity
    * JavaScript: Used to enhance interactivity by manipulating the DOM and enabling dynamic features like form validation, quantity updates, and cart previews.
    * jQuery: Simplifies JavaScript implementation for tasks like AJAX calls and event handling.

* Templating
    * Jinja: The templating language used in Django to pass data from views.py and models.py to HTML templates for rendering dynamic content.

* Deployment and Storage
    * Heroku: Deployment platform to make the website available publically
    * AWS S3: Used for storing and serving static files (e.g., CSS, JavaScript) and media files (e.g., product images).

* Payment Integration
    * Stripe: Integrated to handle secure and user-friendly online payments.

These technologies collectively power the development and delivery of the Smart Tech platform, ensuring a responsive, scalable, and secure experience for users

## Resources

Media:
* pictures and descriptions were takes from:
    * [Currys](https://www.currys.co.uk/)
    * [Pexels](https://www.pexels.com/)

Marketing:
* Newsletter subscriptions and business page were made made using platforms: 
    * [Facebook](https://www.facebook.com/)
    * [Mailchimp](https://mailchimp.com/)

Content:
* For help in setting up the layouts
    * [MDBootstrap](https://mdbootstrap.com/docs/)
    * Boutique Ado project of Code Institute walkthrough

