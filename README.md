# Website-made-with-Flask-and-SQLite

### Goal: 
Making a local-host functional site that is both interactive and beautiful-looking. 
The site is dedicated to facilitating cat adoptions.

### Means:
<strong>Flask: </strong> In order to make the site interactive, the back-end technology used is Flask, in Python. Flask-Forms capture the information submitted by the user and send it back to be proccessed accordingly in index.html. There, more templates are waiting to be called, in order to populate the page when the user clicks on the links in the page.
<strong>Bootstrap: </strong> The site is responsive due to the use of Bootstrap classes.
<strong>SQLite: </strong> Data introduced by users remains stacked in a database, to be accessed once again when the session restarts.
<strong>smtplib: </strong> In order to send messages of to-be-owners to the people who are putting the cats towards adoption, real email messages will be sent at the address given in the forms, using the library smtplib.
