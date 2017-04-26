# PU-Gruppe-25

1.. Installation and Execution
2.. Unit testing instructions

*********************************
* 1. INSTALLATION AND EXECUTION *
*********************************

How to run the application (example for mac, windows do the equivalent in your terminal):

Requirements --> python 3.5 (or newer) and pip --> https://www.python.org/downloads/
Make sure that Python is added to PATHs, in the terminal.

Clone the directory from git hub, link --> https://github.com/sp3kk/PU-Gruppe-25
Make sure the folder is not in readonly, but editable.

In your terminal, move to the directory where you cloned the project
--> cd PU-Gruppe-25/

Then run the following command 
--> pip install -r requirements.txt

Now enter the directory where the manage.py file is located 
--> cd pekka*

You are now all set and can run the project by entering the following command 
--> python3.5 manage.py runserver

To view the application, open your preferred web browser and access the server
--> localhost:8000

********************************
* 2. UNIT TESTING INSTRUCTIONS *
********************************

Requirements: the project folder itself, python3.5 (or newer), and pip.

In the terminal, install coverage.py by entering --> pip install coverage

In the terminal, enter the project folder \%some_folder%\PU-Gruppe-25\

Enter the following lines:

cd pekka*

coverage run manage.py test

coverage report

Output should be a table of files used in tests, test coverage for each,
and total test coverage.
