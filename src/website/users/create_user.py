from src.website.db import user_db_connection
from flask import redirect
import re

class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

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


    def check_if_user_exists(self, email, password, user):
        if user:
            print("This email has already been registered.")
        elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            print('Invalid email address')
        elif not email or not password:
            print('Please fill out the form')
        else:
            return None

    def create_user_if_not_exists(self,db, connection, name, email, password):
        db.insert_new_user(connection, self.name, self.email, self.password)
        db.commit_to_database()
        print("New user created successfully.")