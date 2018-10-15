Bug Killer

A Superhero Themed code solver app
Super fast problem solving code sight for people to post there coding issues for any language. 

UX

This website is for anyone at any level that is having problems with there code in any languages. 
The user will first register and after that sign in. One the user is signed in they can start posting issues.  
If they want a fast response with 24 hours they will have to pay using the products page or the upgrade button in the post detail page. 
All other posts will be treated as a first in first out logic.  
Django built-in  app like 404 pages 

Heroku hosting
https://bug-killer-app.herokuapp.com/

Wireframes can be found in docs folder/ wireframes

User Story
One.    The user signs in or registers if not already done so.
Two.    They go to post an issue. Here they can post a problem they are having. 
        The title of their issue. Give a description of the problem and can add an image to help illustrate it  
Three.  The user will see there post where they can edit it if they feel they are missing something. 
        If they want the issue to be dealt with asap they can press the upgrade button which will bring them to the products page. 
        Pressing the profile button, will bring them to the my issues page where they can see all there logged issues. 
Four.   My Issues tab is where the user can find all their stored posts. 
                Here they can post another issue and go into post detail where they can edit and see feedback from the admin.  
                They can go back to there profile page or go to the upgrade page. 
                All the user's posts will be saved and it is up to the user if they wish to delete them.
Five.   Pressing the upgrade button will bring the user to the products page where they can pay for a faster response. 
Six.    Payment is handled with stripe.  Once the user has press add they are brought to the cart page. 
Seven.  Checkout brings the user to the final stage where they pay. 
        The user will see the product that they have chosen, quantity, price per product and total price if more than one has been purchased. 
        After completing the purchase an alert message will appear notifying the user of the purchase. 
        They are brought back to the products page.


Features
A user is able to log in and register using bootstrap 4 modal 
A simple easy to follow form where users can upload an image, tag the form to link to others. 
My Issues tab where all posts are stored, here a responsive collapse list making it easier for a person to flick quickly through a list of posted issues.
Products page that will allow the user to purchase free or paid for coding help. 
Responsive design that allows to be viewed on any device. 
Feedback 
A status will be given to each post and feedback can be written in as admin that will appear for the chosen post.
Superhero theme running throughout the sight with a self-aware humor 

Features Left to Implement
Search App
It would have been nice to properly implement the search app. To pick up keywords from the user's posts so they could quickly find their issue.

Alert messages
I would have preferred to style them using Django message framework

Profile 
The profile page (my issues) I would have liked to include a strong profile card.
Where the user could put their picture in link there GitHub and slack accounts. It would make it easier for the problem solver to communicate with the user. 

Technologies Used
Jquery: DOM manipulation
Font-Awesome: Cart image and others for products and profile cards
Bootstrap 4: styling and functionality.
Stripe: Payment usage and completion. 
Django: Building modules, using database and admin tool.
Python: Back end


Testing
Throughout ou the building of this project I would save any changes I made, refreshed the website page, checking that everything had changed as expected. 
If it did not then would check an error message if there was one or amend problem as needed.

Manual Testing
Screen shots of error messages can be found in doc/error messages

Forms 
Whether it be a styling issue or a button not responding, the following steps were taken. 
Press form button (login, logout, register, Post issue)
Enter in test details
Press the submit button. This would sometimes not respond or I would get an error. 
Invalid ingenter for the checkout page linked to stripe form. 
It turned out I was missing total = 0 on line 26 in view.py I found this out by going through my code and comparing it against the code institute example. 

Users
I tested if the posts linked up with the user account under a different username. I found that they were not and I had to link them manually as admin on the Django dashboard. 
Correctly linking the posts to the accounts app solved the problem. This was fixed by importing user in into the post model.
Inserting the correct code ForeignKey to the class Post. 
Importing the Post class into the views on the account side, linking it to the user_profile function.

After setting up Travis CI testing I was getting two error messages with media and django version.

Media error
Was caused by having the /media/img on the backend side where I had another folder called media already. I found the fix by removing the /media/ from the code and just having img. 
Reloading the pictures on the admin side in the products app fixed the problem.  

Django version
I received a mail from Github saying "One of your dependencies may have a security vulnerability".  
Asking follow students what it meant as I had never seen a message like that. I made a new branch on my GitHub and made a clone of my work on cloud 9 
Then amended my requirements .txt file for a different version on Django and recommitted my requirements file. 

Linking classes together
for the Post and Status classes, I was having an issue getting the posts to come up on the status model. 
Following the documentation from django to follow a one to one relationship.  
A problem I had that did not through up errors was I using def unicode rather than def __str__ which meant I was just getting an object rather than the title or status. 

Responsive Design 
To check that all devices would see the page correctly. I resized the page manually and used the toggle device tool to see what it would look it. 

Deployment
Running the code locally is entering the command workon foo then entering the command run. 

Launching the project on Heroku 
When setting up secret key I had not put the path in ".." 
Once I had corrected that I was given an error message of unable to follow path which leads to me the incorrect naming of the app on Profile. 
I had incorrectly named app as bug_killer rather than bug.  

Credits

Media
Images
simple bug image. 
https://pixabay.com/en/destroyer-insect-killer-bug-35127/

Superhero
https://pixabay.com/en/superhero-girl-speed-runner-534120/

tshirt
https://www.pexels.com/photo/person-wearing-superheroes-printed-t-shirt-701771/

superhero-outline
https://pixabay.com/en/superhero-human-being-power-alive-450419/

Acknowledgements
The inspiration for the project came from the brief of the assignment and to my own humor on it. I decided on a superhero theme.

For help understanding erros and how to go about fixing them the following people were a great help. 
Jim Richmond
Haley Schafer
Andres Correa

[![Build Status](https://travis-ci.org/Simonbiker/bug_killer.svg?branch=master)](https://travis-ci.org/Simonbiker/bug_killer)

