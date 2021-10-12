# CHARITY FOR GENTLEMEN     
- A fullstack Django website. 
- It's going to be charity platform built up on selling exclusive clothes. All profits goes to Star for life, Water organizations or other charity organizations. The consumer will make a choice of what he or she prefers the profits of his or her order goes to.
- The platform will be focusing a lot on the design and functionality.

<hr>
<br>

# WIREFRAMES

<br>

<a href="" target="_blank"><img src="/documentation/Desktop-MS4-Wireframes.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/documentation/Ipad-MS4-Wireframes.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/documentation/Mobile-MS4-Wireframes.png" alt="Book Bites mobile Sc"> </a>

<br>
<hr>

# DATABASE SCHEMA

<br>

<a href="" target="_blank"><img src="/documentation/Database-schema.png" alt="Book Bites mobile Sc"> </a>

<br>
<hr>

# REASONS FOR DEVELOPMENT
 
* I (Colin Hammarberg) am developing/building this application to create an E-commerce store that offers high end and exclusive clothing to support charity. With all profits going to the charity of the customers choice, we are able to create a beatiful supplyment of clothing, but at the same time support charity organizations all around the world.

<br>
<hr>

# UX
* As an everyday client I want to experience a User Friendly application that is easy to understand and take usage of.
* I want the users to experience a well developed e-commerce platform, that will support their fine taste of clothes and at the same time do something good for the community and world with picking a charity organization when they place their order.

<br>
<hr>

# USER STORIES
<a href="" target="_blank"><img src="/media/plan.png" alt="Book Bites mobile Screen"></a>

<br>
<hr>

# TECHNOLOGIES USED 
 
### HTML
* The project uses HTML to get the visual content.
 
### CSS
* The project uses CSS to design all pages. The project mostly uses bootstrap classes to achive the structure and design, but external CSS too.

### JAVASCRIPT
* The project uses Javascript.

### JQUERY 
* The project uses jQuery.

### PYTHON
* The project uses Python to build the actual applications.
 
### FRAMEWORK
* The project uses Bootstrap 4, to achive a very well functioning framework, responsiveness and helpful tools/classes/grids.

### HEROKU
* Heroku is a cloud platform based on a managed container system, for deploying and running modern apps. I deployed the project to Heroku.

### DJANGO
* The project is built using Django.

### FONTAWESOME
* Font Awesome is an icon toolkit, which I used for the icons visible in the project.

### DATABASE
* PostgreSQL is one of the absolutely most popular relational database management systems. I transfered my database from   SQLite to PostgreSQL when I was deploying my website to Heroku.

### AWS
* I used AWS which offers a cloud storage services to support applications.
#### S3
* Amazon Simple Storage Service (Amazon S3) is an object storage which I used to store my media files.
#### IAM
* AWS Identity and Access Management (IAM) was used to manage access to AWS services and resources securely.
#### BOTO3
* Boto3 is an AWS SDK which allows an easy integration with Python applications with AWS services.
 
### LANGUAGES
* The project uses English as its standard language and an Lang=”en” attribute has also been implemented.

<br>
<hr>

# FEATURES

## EXISTING FEATURES

### HOME & NAVIGATION BAR

<a href="" target="_blank"><img src="/documentation/Home.png" alt="Book Bites mobile Screen"></a>

- The navigation bar is featured on all pages, but in different ways. If a user has not yet created an account and is currently logged into his/hers account, some of the application's features are not visible. The navigation bar is responsive and includes links to the "Gentlemen" logo, Home/Landing page, My Account page, Shop page, Shopping page, About page and Checkout page. The navbar also includes features which will allow the user to login, register and logout. It is identical in each page to allow for smooth navigation throughout the whole application.
- This nav bar will allow the user to easily find him or herself all around the application. As does the mobile navigation drop down.

### ABOUT

* The About page displays information about the company and the work it does. 

<a href="" target="_blank"><img src="/documentation/About.png" alt="Book Bites mobile Screen"></a>

### PRODUCTS

* The Product page displays all of the available products in the database in different columns. The user is also able to filter the products to price (low to high), categories or to view all of the products available.

<a href="" target="_blank"><img src="/documentation/Products.png" alt="Book Bites mobile Screen"></a>

### PRODUCT DESCRIPTION

* The Product Description page displays the chosen product's intel and description. The user is also able to choose what size and in what quantity he or she wishes to receive.

<a href="" target="_blank"><img src="/documentation/Product-Description.png" alt="Book Bites mobile Screen"></a>

### SHOPPING CART

* The Shopping Cart page displays what the user has added to his or her cart. All of the items and selections are displayed in the cart. The user is also able to confirm that he or she would like to place the order and then the user will be directed to the Checkout page.

<a href="" target="_blank"><img src="/documentation/Shopping-Cart.png" alt="Book Bites mobile Screen"></a>

### CHECKOUT

* The Checkout page is where the user is able to place the order. The order details are displayed and the user is able to confirm the order with his or her shipping address and credit card to actually place the order.

<a href="" target="_blank"><img src="/documentation/Checkout.png" alt="Book Bites mobile Screen"></a>

### ACCOUNT

* The user is able to get his or her account details displayed on the "My Account" page. The user is also able to update the details whenever he or she wishes to do so. This makes it easy for the user to place another order, because the user details are already saved in the database.

<a href="" target="_blank"><img src="/documentation/Account-2.png" alt="Book Bites mobile Screen"></a>

### ORDER SUCCESS

* Ones the order has been placed, the user will be directed to a page with the order details. The user is able to checkout what he or she has ordered. It is also a confirmation of that the order has been accurately placed and processed. 

<a href="" target="_blank"><img src="/documentation/Order-success.png" alt="Book Bites mobile Screen"></a>

### PREVIOUS ORDER

* The user is able to view his or her orders on the "My Account" page. This function displays every item which exists in his or her order.

<a href="" target="_blank"><img src="/documentation/Previous-order.png" alt="Book Bites mobile Screen"></a>

### REGISTER

* Before the user is able to purchase any products, he or she has to register an account. The account details are registered in our database and all of the personal details registered in the database is displayed on the "My Account" page. 

<a href="" target="_blank"><img src="/documentation/Register.png" alt="Book Bites mobile Screen"></a>

### LOG-IN

* The user who already has an account registered in the database will be able to log in to his or her account on the log-in page.

<a href="" target="_blank"><img src="/documentation/Log-In.png" alt="Book Bites mobile Screen"></a>

### FOOTER

* The footer contains information about the company and some buttons which leads to different pages on the application.

<a href="" target="_blank"><img src="/documentation/Footer.png" alt="Book Bites mobile Screen"></a>

<br>
<hr>

# TESTING

<br>
<hr>

### I have been conducting tests on the developed application. I had to do lots of testing and it required quite a lot of time. The tests that I have been conducting are the following.

<br>

#### HOME PAGE (Macbook Air M1 + External Screen)
* The landing page has different shades. One where the user has not yet been logged in and I have made sure that only the pages visible then are (Home, About, Register & Log-in). This is made because the user has not yet registered and is not allowed access to any other pages at the time. 
* In the second shade of the landing page, the user has logged in and the home page is still visible. But in the second shade, the user is able to go to the following pages (Home, About, My Account, Shop, Logout, Shopping Cart and the Checkout page.)

<br>

#### ABOUT PAGE (Macbook Air M1 + External Screen)
* The about page button in the navigation bar takes the user to the accurate url.
* The About page tells the user more about the company and offers external links, which are all working fine.

<br>

#### MY ACCOUNT (Macbook Air M1 + External Screen)
* The My Account page saves the user’s personal details after the user has placed his or her first order. That functionality works very well.
* The user is also able to update his or her personal details via the My Account page.  
* The user’s previous order is being correctly displayed on the My Account page too. 
* I have also been conducting tests for the navigation bar, and all links/urls are working fine. 

<br>

#### REGISTER (Macbook Air M1 + External Screen)
* The register functionality has been used and provided by Django. 
* I have made sure that when a user has registered, a confirmation email is sent to the accurate email address. 
* The user is afterwards taken to the log-in page, and is able to log in. The functionality seems to be working exceptionally well.

<br>

#### LOG-IN  (Macbook Air M1 + External Screen)
* The log-in functionality works well too and finds the user’s details (if it exists) in the database. 
* I have also made sure that the navigation bar works fine.

<br>

#### SHOP (Macbook Air M1 + External Screen)
* The shopping functionality works fine too. I have been testing adding products to the shopping cart.
* I have also made sure that all products available are displayed on the products page. 
* All of the buttons seem to be working fine too and acquires the accurate functionality. 
* Even here, I have been testing the navigation bar to see that everything works fine.
* When pressing a button, the page takes the user to the product description page. This works fine too and includes all the accurate information from the database.

<br>

#### SHOPPING CART (Macbook Air M1 + External Screen)
* When a user adds a product to the shopping cart, all of the accurate information is being displayed. The shopping cart also includes buttons for the user to confirm the order and access the checkout page.
* I have also been testing so that the navigation bar links are working fine here too.

<br>

#### CHECKOUT PAGE
* When a user confirms the order in the shopping cart, he or she will access the checkout page. 
* The checkout page contains an order gathering of the items chosen by the user.
* The user is able to confirm and place the order by adding his or her details (name and shipping details + credit card information). I have been testing so that the stripe integration works fine. The tests have been made with stripes testing credit card numbers.
* I have also been testing so that the navigation bar links are working fine here too.

<br>

#### ORDER CONFIRMATION (Macbook Air M1 + External Screen)
* Once the order has been successfully placed, the user is directed to an order success page. This process works fine and the user is taken to the accurate url. 
* I have also made sure that the order success page contains all the correct details from the order.
* I have also been testing so that the navigation bar links are working fine here too.

<br>

#### MESSAGES (Macbook Air M1 + External Screen)
* The application also contains messages for errors, success etc. I have contained tests, to make sure that the messages are working correctly.
* All of the success and error messages are displayed on an accurate occasion.
* I have also been testing that the user is able to close the message down via the “X -close” button.

<br>

#### Responsiveness (Mobile & Ipad Pro Screens)
* The application's responsiveness and framework has also been tested on all pages using both the inspect selection through Google Chrome and on the actual devices (Iphone X, Iphone 8 & Ipad Pro).

<br>
<br>
<a href="documentation/TESTING PROCEDURE.pdf">Download my testing procedure document as PDF</a>
<br>
<br>
<hr>

# FEATURES LEFT TO IMPLEMENT
* In the future I would like to integrate some API or something alike, to give the user the option to view their order status.

<hr>

# DEPLOYMENT

## WHILE DEVELOPMENT

* The application was tested in an environment with Djangos debug mode (in settings.py: Debug=True). The Debug mode is a great thing to have while developing. The reason for using DEBUG=True of debug mode is the displaying of detailed errors on the different pages.

## WHEN DEPLOYING APPLICATION

* In the GitHub terminal, I created a requirements.txt file by running the command (pip3 freeze --local > requirements.txt).

* In the Github terminal, I created a Procfile by running the command (echo web: python app.py > Procfile). According to <a href="https://devcenter.heroku.com/articles/procfile"><b>Heroku</b></a> a Procfile is a mechanism for declaring what commands are run by my application’s web dynos (lightweight Linux containers dedicated to running my application web processes) on the Heroku platform.

* I then logged in to my Heroku account and created the app (charity-for-gentlemen). I also linked my Github repository to receive automated deployment to my Heroku app when pushing my code to Github.

* On Heroku, I went into the Settings tab and accessed the Config Vars. I then entered all variables I had referred to locally in my environment file during development.

* I then uploaded my media files to <a href="https://aws.amazon.com/"><b>AWS (S3)</b></a>. I added the needed environment variables (AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY) in order to access my AWS bucket and the uploaded data. I made sure to use the COLLECTSTATIC command to access and get all of my local static files and bring them to the database. I then disabled the collectstatic (DISABLE COLLECTSTATIC) during a deploy by Heroku by adding in the Config Vars DISABLE_COLLECTSTATIC = value 1.

* I then made a comment to my local database and also include the link to the Heroku generated PostgreSQL database instead. I initialized the PostgreSQL database and pushed the migrations. I used the module dj_database_url within my Django project so that I could refer to a url directly in my settings.py.

* I then changed the "DEBUG=True" option in my settings.py to "DEBUG=False", which means that I changed the app environment to production.

* I requested the deployment from the branch master and reviewed the logs via the Heroku dashboard during the deployment. Once it was done deploying to Heroku, I tested so that everything had been deployed accordingly and to make sure everything worked smoothly.

* <a href="https://charity-for-gentlemen.herokuapp.com/">Deployed Version (Heroku App)</a>
<br>
<hr>

# MEDIA

### PRODUCTS
<br>

* All images used on Charity For Gentlemen were found Best Secret. Down below you are able to find all links to the owner (Best Secret) of all images.
<br>

- https://picture.bestsecret.com/static/images/1519/image_31991066_42_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1518/image_31991066_30_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1584/image_32072735_36_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1584/image_32072735_36_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1589/image_32081445_73_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1611/image_32097841_30_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1563/image_32029879_70_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1559/image_32030026_30_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1563/image_32029949_88_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1582/image_32051744_42_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1582/image_32051744_42_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1559/image_32029993_71_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1559/image_32029993_71_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1559/image_32029993_71_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1539/image_32012613_31_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1538/image_32012611_44_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1590/image_32070182_80_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1590/image_32070182_36_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1588/image_31992448_99_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1529/image_31992448_10_620x757_0.jpg
- https://picture.bestsecret.com/static/images/596/image_30801570_10_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1647/image_32074297_75_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1647/image_32134619_10_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1530/image_32018216_70_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1549/image_32030652_21_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1553/image_32030650_59_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1561/image_32029979_31_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1649/image_32012521_71_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1192/image_31652159_34_620x757_0.jpg
- https://picture.bestsecret.com/static/images/1192/image_31652160_72_620x757_0.jpg

<br>

### HOME
<br>

- http://bespoketailors.pk/assets/uploads/57a06-suit.jpg

<br>

### ABOUT US PAGE
<br>

- http://bespoketailors.pk/assets/uploads/57a06-suit.jpg
- https://images.pexels.com/photos/7265994/pexels-photo-7265994.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
- https://images.pexels.com/photos/460672/pexels-photo-460672.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
- https://images.pexels.com/photos/2695680/pexels-photo-2695680.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
- https://images.pexels.com/photos/2695680/pexels-photo-2695680.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
- https://images.pexels.com/photos/2190283/pexels-photo-2190283.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
- https://images.pexels.com/photos/1529040/pexels-photo-1529040.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260

<br>
<hr>

# CREDITS
- Footer section was inspired by Bootstrap 4 examples.
- Had a difficulty remembering the checkout code structure and was inspired by Code Institute's mini project to finally get it to work accordingly.
- I would also give much credit and acknowledgement to Code Institute's lessons and the huge benefit to go back and look at the lessons again to both find inspiration and to fix potential bugs. It has been such a helpful tool for me and I would like to give huge credits to Code Institute for creating such an amazing structure and benefit.
- 

<br>
<hr>

# ACKNOWLEDGEMENTS
- I would like to acknowledge Code Institute's tutor support which has been a huge benefit and has helped me along whenever I needed it. Thank you for that!
- I would also like to thank every single individual who has looked at my project and given me constructive feedback, along with always supporting me. Thank you!

<br>
<hr>

# CODE VALIDATOR
* The code has been searched for errors through the validators mentioned below.
- HTML Validator (https://validator.w3.org/)
- CSS Validator (https://jigsaw.w3.org/css-validator/)
- Python Validator (http://pep8online.com/)
- Javascript Validator (https://esprima.org/demo/validate.html)

<br>
<hr>

# PUSH TO GITHUB

* The entire code has been written on GitPod and later on pushed to GitHub.
* When I push my code to GitHub from GitPod I'm writing five different steps in my terminal. 
1. The first step that I always do is to save the code (by pressing "save all"). 
2. The second step that I always do is to run "git status". This gives me an overview of which files I have left to push and save to GitHub. 
3. The third step that I always do is to run "git add" and then followed by the file or folder that I would like to add. 
4. The fourth step that I always do is to run "git commit -m "Here I write a comment. So that my commits to GitHub are well documented along the way. That makes it a a lot easier to locate which commit I have been making when looking back at them".
5. The fifth and last step that I always run in my terminal is just a simple "git push". This takes all of the files that I have added and then afterwards commited and pushes them all to GitHub (where the files and all of the code will be stored in a proper way).

<br>
<hr>

# CLONING

### Cloning Github Code by downloading ZIP code
* If you wish to clone my code (which is a public published code) you are free to do so. Please follow the steps down below to accomplish the cloning procedure:
1. Copy this link and place it in a new window (https://github.com/ColinHammarberg/Milestone-project-4). 
2. Click on the "Code" button and select "HTTPS" to get the required options for cloning. 
3. Click on the "Download ZIP" to download the code files in ZIP format. 

### Cloning Github code by terminal
1. Copy this link and place it in a new window (https://github.com/ColinHammarberg/Milestone-project-4). 
2. Click on the "Code" button and select "GitHub CLI" to get the required options for cloning. 
3. Copy the text "gh repo clone ColinHammarberg/Milestone-project-4" and place it in your terminal. 
4. Press enter and it should begin downloading accordingly.