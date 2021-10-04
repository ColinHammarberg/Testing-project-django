# CHARITY FOR GENTLEMEN     
- A fullstack Django website. 
- It's going to be charity platform built up on selling exclusive clothing & cigars. All profits goes to Star for life, Water organizations or Planting trees. The consumer will make a choice of what he/she prefers the profit goes to.
- The platform will be focusing a lot on the design and functionality.


# WIREFRAMES

<br>
<a href="" target="_blank"><img src="/documentation/Desktop-MS4-Wireframes.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/documentation/Ipad-MS4-Wireframes.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/documentation/Mobile-MS4-Wireframes.png" alt="Book Bites mobile Sc"> </a>

<br>
<br>

# UX
 
* As an everyday client I want to experience a User Friendly application that is easy to understand and take usage of.
* The visitor is the individual who is a client of LOVE THERAPY. The application helps the client to get a better structure. 
* They will experience an ordinary, but different kind of application page. Not too much focus on the design, but more focus on the actual data and functions.

# REASONS FOR DEVELOPMENT
 
* I (Colin Hammarberg) am developing/building this application to create an E-commerce store that offers high end and exclusive clothing to support charity. With all profits going to the charity of the customers choice, we are able to create a beatiful supplyment of clothing, but at the same time support charity organizations all around the world.

<a href="" target="_blank"><img src="" alt="Book Bites mobile Screen"></a>

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

### DJANGO
* Heroku is a cloud platform based on a managed container system, for deploying and running modern apps. I deployed the project to Heroku.

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

# FEATURES

## Existing Features

### Navigation bar 
<a href="" target="_blank"><img src="/media/Navbar.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/media/Mobil-navbar.png" alt="Book Bites mobile Screen"></a>

- The navigation bar is featured on all pages, but in different ways. If a user has not yet created an account and is currently logged into his/hers account, some of the application's features are not visible. The navigation bar is responsive and includes links to the "Gentlemen" logo, Home/Landing page, My Account page, Shop page, Shopping page, About page and Checkout page. The navbar also includes features which will allow the user to login, register and logout. It is identical in each page to allow for smooth navigation throughout the whole application.
- This nav bar will allow the user to easily find him or herself all around the application. As does the mobile navigation slide out.

# MEDIA
- https://www.pexels.com/sv-se/foto/restaurang-vintage-cigarr-lyx-7299582/

# CREDITS
- The Checkout models.py & Admin.py is completely inspired by Code Institute and I would like to thank them for that!

# DEPLOYMENT

## WHILE DEVELOPMENT

* The application was tested in an environment with Djangos debug mode (in settings.py: Debug=True). The Debug mode is a great thing to have while developing. The reason for using DEBUG=True of debug mode is the displaying of detailed errors on the different pages.

## WHEN DEPLOYING APPLICATION

* I then logged in to my Heroku account and created the app (charity-for-gentlemen). I also linked my Github repository to receive automated deployment to my Heroku app when pushing my code to Github.
* On Heroku, I went into the Settings tab and accessed the Config Vars. I then entered all variables I had referred to locally in my environment file during development.
* I then uploaded my media files to AWS (S3). I added the needed environment variables (AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY) in order to access my AWS bucket and the uploaded data. I made sure to use the COLLECTSTATIC command to access and get all of my local static files and bring them to the database. I then disabled the collectstatic (DISABLE COLLECTSTATIC) during a deploy by Heroku by adding in the Config Vars DISABLE_COLLECTSTATIC = value 1.
