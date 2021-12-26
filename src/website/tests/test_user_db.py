# testing the user and db connection
from unittest.mock import patch
import unittest
from src.website.db.user_db_connection import userAccountDbConnection


class connection:
    def execute(self):
        return True


class TestUser(unittest.TestCase):
    @patch('src.website.db.user_db_connection.MySQL')
    def test_connect_to_database(self, sql):
        sql.connection.cursor.return_value = 'sql'
        response = userAccountDbConnection.connect_to_database()
        self.assertIsNotNone(response)

    @patch('src.website.db.user_db_connection.MySQL')
    def test_commit_to_database(self, sql):
        sql.connection.commit.return_value = 'sql'
        response = userAccountDbConnection.commit_to_database()
        self.assertIsNone(response)

    def test_create_user_table(self):
        response = userAccountDbConnection.create_user_table(conn=connection)
        self.assertTrue(response)
