#!/usr/bin/python3
"""Unit test module for User """
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """test cases for the User model """

    @classmethod
    def setUpClass(cls):
        """setup for test"""
        cls.user = User()
        cls.user.first_name = "User1"
        cls.user.last_name = "Userf"
        cls.user.email = "user1@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """removes instance at the end of the test"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_first_name(self):
        """testing user first_name attribute """
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name(self):
        """ testing user last_name attr"""
        self.assertEqual(type(self.user.last_name), str)

    def test_email(self):
        """ testing uer email attr"""
        self.assertEqual(type(self.user.email), str)

    def test_password(self):
        """ testing user password attr"""
        self.assertEqual(type(self.user.password), str)


if __name__ == "__main__":
    unittest.main()
