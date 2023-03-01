# Website-made-with-Flask-and-SQLite

## Goal: 
Making a local-host functional site that is both interactive and beautiful-looking. 
The site is dedicated to facilitating cat adoptions.

## Technologies:
+ <strong>Flask: </strong> In order to make the site interactive, the back-end technology used is Flask, in Python. Using render_template, redirect, url_for, main.py becomes the file from which more templates are waiting to be called, in order to populate the page when the user clicks on the links present in index.html. In templates like presentation.html and search.html the information isn't hardcoded into a html structure, but rather it is put into the the right place in the template whenever the page is loading.
+ <strong>wtforms: </strong> WTForms is a flexible forms validation and rendering library for Python web development. I used it to capture the information submitted by the user and send it back to be proccessed accordingly in index.html.
+ <strong>Bootstrap: </strong> The site is responsive due to the use of Bootstrap classes.
+ <strong>SQLite: </strong> Data introduced by users remains stacked in a database, to be accessed once again when the session restarts.
+ <strong>smtplib: </strong> In order to send messages of to-be-owners to the people who are putting the cats towards adoption, real email messages will be sent at the address given in the forms, using the library smtplib.

## How it works:


https://user-images.githubusercontent.com/101098099/222118437-fa8fb935-5237-4b93-829e-0b5a15584433.mp4


## main.py
This is the file that sets the site in motion. I started by creating the Flask, Bootstrap and SQLAlchemy objects. Using FlaskForm, I created classes that will constitute my AddForm, AdoptionForm and the Filter, which will give shape to the forms on the site. I also created a table object named Pisica, which will store cats  in the database.

Using @app.route I tell Flask what routes can be followed on my website. A route like '/search' will redirect the user to the template search.html. At the beginning, however, the site will start at its home root, which makes use of the index.html.
<br/>

## index html
This is the main page. The header and footer are included as templates, while the rest of the html structure is hardcoded. This page consists of a title, buttons towards the 'Adopta' and 'Adauga' pages, a 'features' section, an 'about us' section and a carousel with images.
<br/>

## search.html
This page is accessed through the 'Adopta' button. Besides the header, it contains a 'Filter' button, which shows the three criteria for filtering cats in the database (location, age and color) upon being pressed. Below the area dedicated to the filter, rows of cards are automatically populated with information about cats extracted directly from the database. The cats variable stocks the selected cat objects, and with the help of a for structure multiple cards are populated dynamically.
<br/>

## presentation.html
If a user decides to click on the 'Detalii" button assigned to each cat in the search page, then the route '/presentation' is followed. The cat's id in the database is passed on in this scope to the function presentation() from main.py, which takes care of activating the presentation template. This is the presentation.html file. Here, an already defined structure waits to be filled with information about the given cat. A WTForm  is also set to the right in order to give the user the chance to contact the temporary user of the cat, giving information about himself. Finally, the information submitted will be messaged via email to the owner.
<br/>

## add.html: WTForm - adding a new cat to the database and site
Another use of the WTForms is made in the add.html file, which corresponds to the '/add' route accessible through the 'Adauga' button visible on the home page. The page is very simply and elegantly laid out, asking the user to input the name, age, sex, color, species, and location of the cat, as well as a photo and description, plus contact information. The form returns the information to the add() function in main.py, where it is validated and immediately inserted into the database and onto the site.
