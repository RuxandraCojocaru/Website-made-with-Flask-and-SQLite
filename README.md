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
# main.py
This is the file that sets the site in motion. I started by creating the Flask, Bootstrap and SQLAlchemy objects. Using FlaskForm, I created classes that will constitute my AddForm, AdoptionForm and the Filter, which will give shape to the forms on the site. I also created a table object named Pisica, whih will hold my cats for me in the database.

Using @app.route I tell Flask what routes can be followed on my website. A route like '/search' will redirect the user to the template search.html. At the beginning, however, the site will start at its home root, which makes use of the index.html.

# index html
This is the main page. The header and footer are included as templates, while the rest of the html structure is hardcoded. This page consists of a title, buttons towards the 'Adopta' and 'Adauga' pages, a 'features' section, an 'about us' section and a carousel with images.

https://user-images.githubusercontent.com/101098099/221690986-64983275-db88-4fde-ab79-bb68d5c84626.mp4

# search.html
https://user-images.githubusercontent.com/101098099/221697890-f5b43009-abd7-435a-a77c-854460f22e65.mp4


# presentation.html
https://user-images.githubusercontent.com/101098099/221697978-58fe17a3-fe03-41cc-8e6e-739b3fcfc11f.mp4


# FlaskForm - adding a new cat to the database and directly onto the site



