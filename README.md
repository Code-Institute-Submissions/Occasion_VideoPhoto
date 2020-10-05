# **Occasion Video&Photo** :
This application is a eCommerce website that allows you to buy services online (filming and photograph events) like *Wedding, Engagement, Baptism, Student, first communion*. The type of this eCommerce website
is Business-to-Consumer **(B2C)** which is an electronic transactions of services(filming and photograph event) between *Occasion Vidoe&Photo* and consumers.
The consumer can browse the website and look at products, pictures, read reviews. Then they place their order. Customers are usually asked to place their orders by filling up a form, register
or login if it is an existing customer. They need to provide all the necessary details informations like the address. The payment methods used in this eCommerce website are credit cards. There is a contact page where you can contact
the eCommerce website **Occasion Video&Photo**.

# **UX** :
This application provides a eCommerce website that allows the consumer to browse the website and look at products, pictures, read reviews. Then they place their order. The first thing I have in mind with **UX** application to make it responsive 
**mobile-friendly** web sites, studies are showing that **54%** of online ecommerce traffic comes from a mobile smartphone.
The website has flat design. Navigation is easy to find category and sub-category names. The **search bar** placed in the header on all pages, allow for search by product name,descriptions,things include. 
The **products page** displaying in a context. Reveal interesting product details in **details page** with so many things to consider, *descriptions, things include, rating* and Cart button in a good size, readable
with a color that stands out from the rest of the page. Customer feedback is one thing to keep in mind when doing UX, so therefore I had the **contact page** when they have problems with payment, and if they are wondering or need more explanation for any products.
Check out the **[Mockup](https://drive.google.com/file/d/1wNaWGxL8qOKg0pVDxfa1St1iYqkEodCT/view?usp=sharing/?target=_blank)** that I have created as part of the design process and the design of **[database schema](https://drive.google.com/file/d/1THbnuPw8SWDmFhDM9OuU1RQYjQcgRtzM/view?usp=sharing/?target=_blank)**.
### **User Stories**:
I have put my user stories in a document you can check it out in here **[user stories](https://drive.google.com/file/d/18DqR_RgDAsI-80bcEcClNI3gQysx8ZNc/view?usp=sharing/?target=_blank)** 

# **Features**

## Existing Features:
- There are five general pages home, products, video, photo, contact us, user profile and bag.
- Search bar: to search for a specific production.
- There are some subpages(filter function) under video and photo and products.
- In the header(navbar-menu) I have two icon(user and bag):
  1. User allows users to login or register.
  2. Bag to shows Shopping Bag.
- Admin Dashboard: to be able to the administrative(edit and deletes products,users and orders).
- Authentication user: to give verifying the identity of the users who has register as an Admin or a buyer).

## Features Left to Implement:
- **add reviews**: Allow customers to add reviews.
- **Chat**: Allow customers to live chat if they get some issue when they shop or get stuck.
- **Streaming**:This website is a eCommerce website to buy services online (filming and photograph events) it is just as a good to have 
   such a streaming service in the future.

# Technologies Used:

- Codeinstitute: materials and homework and projector during the lesson.
- Stripe: API payment system.
- Amazon Web Services(AWS S3).
- Heroku: is a cloud platform for deploying.
- Postgres: is a relational database.
- Git: is a distributed version control system.
- Balsamiq Mockups: Sketch and make UI Design for the website.
- HTML: by using HTML language to markup web pages in this project.
- CSS: to perform style for the WepApp.
- Bootstrap 4: to perform style and responsive for the WepApp.
- FontAwesome: to perform font and icon.
- Django: Python Web framework provides a lot of features to build the website.
- Google fonts: to add fonts to the webApp.
- JavaScript and jQuery to perform:
  1. Navbar links.
  2. Mobile Navigation(navbar responsive for the mobile).
  3. Handle realtime validation errors on the card element
  4. Handle form submit.
- Websites like: ( **Stackoverflow** ,  **css-tricks** ,  **w3schools** ,  **github** ,  **youtube** ).

# Testing:
After the Mentor Guidance Session 2 - Middle of project call. Initially, I got some feedback and I made a little change:
- Has changed the button text from **Add To Bag** to **Add To Cart**.
- Price text color has changed to blue.
- Profile - Order history page has separated to two separate pages(**Profile** and **Order History**).
- Has changed products page by make each product as a link(card) and add a button(Add To Cart) for each product in the page.
- Refactoring the Code.

### Django Testing Framework:
Has made some Testing by using **Django testing framework** and create automated tests for all apps in the project by testing (views, forms, models).
Django has a testing framework available that we can use to create automated tests.
That ensure our application is working as expected. When we created created any app it provided us by default
with a *tests.Python* file. Inside this file we'll find that Django imports the test case class. This class is an extension of the Python standard library module called unit tests.
Which provides us with a bunch of methods to assert various things about our code. Such as assert equal assert true assert false and so on.


# Deployment:

I have chosen to deploy my project in **Heroku** and **AWS S3**. Why? I need a server to put my static and media files(AWS S3) and to handle the request which GitHub Pages cannot support at this moment. Heroku offers a lot of features and flexibility, all for free. Some of the benefits include:

- Easy setup(deployment).
- Good cooperation and communication using Git and heroku.
- Free hosting.

## Deployment On Heroku And AWS S3:

### Heroku:
Before we set up AWS though, let's create a Heroku app where the rest of our code can live.
1. **Create App**: Click New on the top right corner and select &quot;Create new app&quot;. Give the application a name (This will be included in the public URL for the application) and click Create app.
2. **Postgres database**: Then on the resources tab, I'll provision a new Postgres database. To use Postgres we need to install dj_database_url, and psycopg2.
3. **Creating a connection between our Gitpod application and Heroku**: Now we open the project in Gitpod. Login to Heroku through terminal. We are creating a connection between our Gitpod application and Heroku
that would allow us to push our changes using Git to update the application at any given time.
4. **Create a new Git repository**: Create a new Git repository using git init. And then is add our files to the repository.
5. **Associate the Heroku application**: To associate the Heroku application as our master branch, or remote master branch we have to use those tow commands *(1. heroku git:remote -a production-management. 2. git push heroku master)*.
6. **Requirements text**: Now we need the requirements text will contain a list of the applications that are required for Heroku to run the application.
7. **Procfile**: is also needed to get our application live in Heroku. The Procfile is an instruction to Heroku as to which file is used as our entry point at the application, which file we use to call the application to get it up and running.
So we have write this command (heroku ps:scale web=1) over to the Heroku app to tell it to get up and running.
8. **Settings file**: By going to settings file and importing dj_database_url.Then down in the databases setting. I'll comment out the default configuration.
And replace the default database with a call to dj_database_url.parse and give it the database URL from Heroku.
9. **Migrations**: Because we're connecting to Postgres now. We need to run all these migrations again.
10. **Deploys successfully**: Make sure our app deploys successfully and the application should be live before we move on to setting up Amazon Web Services.

### Amazon Web Services(AWS S3):
With our app deploying to Heroku we're almost done. But we need a place to store our static files and images.
For this, we're going to use **Amazon Web Services s3** and create an AWS account.
1. **S3 and Create A Bucket**: Accessing the AWS management console under my account. And search S3 service. Open s3 and create a new bucket. Which will be used to store our files.
2. **Generate Policy**: Now we need to set a few basic settings on our new bucket to generate policy. Bucket policy and course configuration will now allow full access to all resources in this bucket.
3. **Public Access**: Set the list objects permission for everyone under the Public Access section.
4. **Create a user to access Bucket**: Through service called IAM which stands for Identity and Access Management. first create a group for our user to live in.Then create an access policy giving the group access to the s3 bucket we created.
And finally, assign the user to the group so it can use the policy to access all our files.
5. **Connecting Django To S3**: To do this we'll need to install two new packages on our Django project **boto3** And **django-storages**. We need to add some settings in settings file
to tell it which bucket it should be communicating with.
6. **AWS Keys**: Let's go to Heroku and add our AWS keys to the config variables.
7. **Add media files to s3**: On s3, create a new folder called media.
Inside it, I'll click upload. Add files. And then select all the product images.





