# Website-made-with-Flask-and-SQLite

## Goal: 
Making a local-host functional site that is both interactive and beautiful-looking. 
The site is dedicated to facilitating cat adoptions.

## Technologies:
+ <strong>Flask: </strong> In order to make the site interactive, the back-end technology used is Flask, in Python. Using render_template, redirect, url_for, main.py becomes the main file from which more templates are waiting to be called, in order to populate the page when the user clicks on the links present in index.html. This means that generally the information isn't hardcoded into a html structure, but rather it is put into the the right place in the template whenever a page is loading.
+ <strong>wtforms: </strong> WTForms is a flexible forms validation and rendering library for Python web development.I used it to capture the information submitted by the user and send it back to be proccessed accordingly in index.html.
+ <strong>Bootstrap: </strong> The site is responsive due to the use of Bootstrap classes.
+ <strong>SQLite: </strong> Data introduced by users remains stacked in a database, to be accessed once again when the session restarts.
+ <strong>smtplib: </strong> In order to send messages of to-be-owners to the people who are putting the cats towards adoption, real email messages will be sent at the address given in the forms, using the library smtplib.
