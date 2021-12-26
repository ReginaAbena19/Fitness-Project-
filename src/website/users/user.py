from src.website.db import user_db_connection
import re

"""
This class is responsible for checking whether a user exists in the database
and creating the user if not. 
"""
class User:
    """
    The class constructor that will initialize all the key variables for the User class
    """
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    """
    This function connects to the database and creates the user.
    """
    def create_user(self):
        db = user_db_connection.userAccountDbConnection
        connection = db.connect_to_database()
        db.create_user_table(connection)

        user = db.check_if_user_exists_in_db(connection, self.email)
        print(user)

        self.check_if_user_exists(self.email, self.password, user)

        if user is None:
            self.create_user_if_not_exists(db, connection, self.name, self.email, self.password)
            return True
        else:
            return False

    """
    This function checks if a user exists if they attempt sign up. 
    """
    def check_if_user_exists(self, email, password, user):
        if user:
            print("This email has already been registered.")
        elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            print('Invalid email address')
        elif not email or not password:
            print('Please fill out the form')
        else:
            return None

    """
    This function inserts the new user to the database. 
    """
    def create_user_if_not_exists(self, db, connection, name, email, password):
        db.insert_new_user(connection, self.name, self.email, self.password)
        db.commit_to_database()
        print("New user created successfully.")
