# MessagingApp

REST APIs have been generate to send and receive anonymous and unanonymous users.

Users shall register at 
`'/account/register` by filling email, username, password, confirm_password
then can then login at
`'/account/login` by filling their email and password

This will generate a token which will help access other functions, and also ability send messages to registered users.

A registered user can send amessage to username_A using his token by going to
`/<username_A>/create`
Entering "text" is compulsory for the same, entering "author" is optional, if any value is entered in author, the username is mentioned as the author, else its empty and message remains anonymous.

Username A can view his list by going to `/<username_A>/list` using his token.
He/She can view and delete particular message by the following URLs
`'<int:pk>/delete'`
`'<int:pk>/detail'`
using his/her token.

## Setup and run

1. Create a virtual environment with Python3.7: `virtualenv env -p python3.7`. If you dont have `python3.7` yet then you can install it with:
    1. linux(ubuntu/debian) - `sudo apt install python3.7`
    2. windows - Download installer from https://www.python.org/downloads/release/python-370/.
2. Activate the virtual environment: `source env/bin/activate`
3. Install all the dependencies in `requirements.txt` file: `pip install -r requirements.txt`
4. Migrate the migrations: `python manage.py migrate`
5. Run the app: `python manage.py runserver`
6. Navigate to http://localhost:8000 in your browser
7. When you are done using the app, deactivate the virtual environment: `deactivate`
