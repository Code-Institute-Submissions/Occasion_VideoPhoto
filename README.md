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
Check out the **[Mockup](https://drive.google.com/file/d/1wNaWGxL8qOKg0pVDxfa1St1iYqkEodCT/view?usp=sharing)** that I have created as part of the design process and the design of **[database schema](https://drive.google.com/file/d/1THbnuPw8SWDmFhDM9OuU1RQYjQcgRtzM/view?usp=sharing)**.
### **User Stories**:
I have put my user stories in a document you can check it out in here **[user stories](https://drive.google.com/file/d/18DqR_RgDAsI-80bcEcClNI3gQysx8ZNc/view?usp=sharing).** 

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
TO DO!!

# Deployment:

I have chosen to deploy my project in **Heroku** and **AWS S3**. Why? I need a server to put my static and media files and to handle the request which GitHub Pages cannot support at this moment. Heroku offers a lot of features and flexibility, all for free. Some of the benefits include:

- Easy setup(deployment).
- Good cooperation and communication using Git and heroku.
- Free hosting.

### Deployment On Heroku And AWS S3:

Click New on the top right corner and select &quot;Create new app&quot;. Give the application a name (This will be included in the public URL for the application) and click Create app.
Now we open the project in Gitpod. Login to Heroku through terminal. What we are doing here is we&#39;re creating a connection between our Gitpod application and Heroku that would allow us to push our changes using Git to update the application at any given time.
Then, we create a new Git repository using git init. And then is add our files to the repository. And then we are going to associate the Heroku application as our master branch,
or remote master branch by using those tow commands (1. heroku git:remote -a production-management. 2. git push heroku master). Now we need the requirements text will contain a list of the applications that are required for Heroku to run the application.
The Procfile is also needed to get our application live in Heroku. The Procfile is an instruction to Heroku as to which file is used as our entry point at the application, which file we use to call the application to get it up and running.
So we have write this command (heroku ps:scale web=1) over to the Heroku app to tell it to get up and running.
And the last step is specifying our IP and our port that the server instance on Heroku will know how to run our Flask application to do that in Heroku home page,
we&#39;re going to go to settings \&gt; click on Reveal Config Vars and on the input field Key we should write IP and in input field Value write the IP address which is in my case(0.0.0.0) and do the same with port:5000 in my case. And click on the top right corner &quot;Open app&quot; and the application should be live.





