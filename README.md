# hcl_employees

This project is meant to be a basic single page web application that displays the contents of a database of employee names and phone numbers.

I used pipenv to create a virtual environment to bootstrap a Flask back API. 

I then used SQLalchemy ORM to integrate the Flask App with a mysql database on a locally hosted mysql server. 

I then installed and used the Angular CLI to create a new single page application for the front end. Currently this SPA fetches and displays employee names
from the back end to show visitors.

To create and start the python virtual environment one simply needs to install pipenv on their local machine and run 'pipenv install' .
This should then download the required dependencies from the pipfile.
