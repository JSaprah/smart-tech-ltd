# smart-tech-ltd

Smart Tech is a fictional B2C electronics store crafted with Django, Python, HTML, and CSS. It serves as a sleek, modern platform for showcasing the newest and trendiest tech products. From must-have gadgets to innovative accessories, Smart Tech lets users explore it all effortlessly. Shoppers can browse the full collection or filter items by category. With a robust search function and a built-in stock management system, customers can shop with confidence.

Once signed in, customers can save their delivery address for a faster checkout process. They can also revisit their order history, making it simple to keep track of previous purchases.

This project was inspired by a love for cutting-edge technology and the dream of creating an online store that connects people with the latest innovations. While that dream evolved, Smart Tech became a showcase project and a valuable tool for learning and mastering Django and Python development.

The deployed site can be visited here: [Smart Tech](https://smart-tech-ltd-89566b21efa9.herokuapp.com/)


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

![class diagram Smart Tech](docs\flowcharts\diagram_smart_tech.PNG)


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

![Home page wireframes](docs\wireframes\wireframe_home.PNG)  


#### Products Page

Focused on showcasing items with intuitive filtering and sorting.

![Product page wireframes](docs\wireframes\wireframe_products.PNG)  


#### Product Details Page

Highlighting essential product information to aid decision-making.

![Product details page wireframes](docs\wireframes\wireframe_product_details.PNG)  


#### Add/edit product page
Add/Edit Product Page: Provides the store owner with a dedicated page to efficiently update the product catalog, ensuring inventory accuracy and relevance.

![Add/edit page wireframes](docs\wireframes\wireframe_product_add_edit.PNG)


#### Shopping bag Page

Ensuring users can easily review and edit their selections.

![Shopping bag page wireframes](docs\wireframes\wireframe_bag.PNG)


#### Checkout Page

Streamlined for quick and hassle-free payment.

![Checkout page wireframes](docs\wireframes\wireframe_checkout.PNG)  


#### Order Confirmation Page

This page provides a clear confirmation that their order has been successfully processed. 

![Order confirmation page wireframes](docs\wireframes\wireframe_order_confirmation.PNG)  


#### User Profile Page

Providing access to user details and order history.

![User Profile page wireframes](docs\wireframes\wireframe_profile.PNG)  

#### Wishlist Page: 

Allows users to save items of interest for later, encouraging thoughtful and repeat purchases.

![Wishlist page wireframes](docs\wireframes\wireframe_wishlist.PNG)

#### Contact Page: 

A simple, user-friendly form for inquiries or feedback, ensuring smooth communication with store administrators.

![Contact page wireframes](docs\wireframes\wireframe_contact.PNG)


These visualizations guided the site's structure while ensuring alignment with user needs and project goals.

When creating the wireframes the sorting dropdown was not taken into consideration. This is an addition for all the product screens.


## Features

### Common to all pages


### Page content


#### Home page

At the heart of the Home Page is a sleek and minimal introduction that captures the essence of the brand. This pages provides a simple call to Action: A prominently placed button labeled “Shop now" invites users to dive right into exploring the product catalog effortlessly.

![Home page mobile](docs\features\mobile\home_page_mobile.PNG)  
![Home page desktop](docs\features\desktop\home_page_desktop.PNG)  



#### Product Page

The Products Page is designed to provide users with an effortless browsing experience to explore the store’s offerings. It combines a sleek layout with functionality to ensure that shoppers can quickly find and sort products tailored to their needs. It mainly covers the user stories for sorting, filtering and viewing all products.

* Search Results Display: Shoppers can easily view search results with the total number of matching items clearly indicated.
* Search Functionality: Responsive search bar allows users to locate products by entering keywords related to the name or description
*Sorting Options: Shoppers can sort results using filters by name, category and price.


#### Add/edit product page

The Add/Edit Product Page is a feature for store administrators to manage the product catalog. This page is designed with simplicity and efficiency in mind, allowing admins to quickly add new products or update the details of an existing product. 

Key features

Add Product:
* Admins are presented with a clean, easy-to-use form to input all necessary product details:
    * Product Name
    * Description
    * Price
    * Category (Headsets, Gaming, Accessories)
    * Image Upload

Edit Product:
Pre-Populated Fields:
* When editing a product, the form is pre-populated with the current details of the selected product.
* This allows admins to quickly identify and adjust the information they wish to modify, such as updating the price or changing the description.

Validation:
Each field is validated to ensure proper formatting, such as requiring non-empty fields and numeric values for price and stock. The form ensures that all updates meet the same validation standards as adding a new product, avoiding incomplete or incorrect entries.


#### Product Details Page

The Product Details Page is designed to provide shoppers with all the information they need to make informed purchasing decisions. This page includes four key sections to streamline the user experience:

* Product Overview: Displays the product's name, price, a detailed description, and an image. Shoppers can select a quantity for purchase directly from this section.

* Reviews: Features a dedicated tab where users can:
    * Read existing reviews to gain insights from other customers.
    * Leave their own review and assign a star rating to share their experiences with the product.
    * For authenticated users, options to delete previously submitted reviews are included, allowing opinions removed as needed.

* Wishlist Integration: A heart icon enables users to instantly add the product to their wishlist with a single click, making it easy to save items for future consideration.

* Admin Controls: Superusers are empowered to:
    * Edit product details directly from this page, such as descriptions, pricing, or stock status.
    * Remove products from the store inventory that are no longer available for sale.


#### Shopping Page

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


#### Order confirmation page

The Order Confirmation Page serves as the final step in the shopping journey, ensuring customers feel assured and informed after placing an order. This page provides a clear confirmation that their order has been successfully processed. Key details displayed include:

* A confirmation message thanking the customer for their purchase.
* The order number for easy reference
* A summary of the purchased items, including quantities and prices.
* Additionally, users will receive an email confirmation with these details, providing a record of their transaction for future reference.


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


### Contact page

The Contact Page is designed to facilitate seamless communication between users and the store’s support team. It prioritizes simplicity and accessibility, allowing customers to submit inquiries, feedback, or any concerns effortlessly.

It consists of a user-friendly form; includes fields for:
* Name
* Email Address
* Subject
* Message