This project is an assignment in course "Capstone: Retrieving, Processing, and Visualizing Data with Python"

Using the Google Places API with a Database and Visualizing Data on Google Map.
In this project we take our input data in the file
(where.data) and read it one line at a time, and retrieve the
geocoded response and store it in a database (geodata.sqlite).

We execute the geoload.py. This code reads where.data (this file contains names of different places), 
after that, using API http://py4e-data.dr-chuck.net/json? given by course, we
retrieve the data and store it in the database.

Next step is to visualize the data using the (geodump.py) program.
This program reads the database and writes tile file (where.js)
with the location, latitude, and longitude in the form of
executable JavaScript code.
The file (where.html) consists of HTML and JavaScript to visualize
a Google Map.

After executing geoload.py and geodump.py we can open where.html 
(this file consists of HTML and JavaScript to visualizea Google Map)
to see the locations in a browser.
