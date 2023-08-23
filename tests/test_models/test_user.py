#!/usr/bin/python3
"""Unit test module for User """
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """test cases for the User model """

    @classmethod
    def setUpClass(cls):
        """setup for test"""
        cls.user = User()
        cls.user.first_name = "User1"
        cls.user.last_name = "Userf"
        cls.user.email = "user1@gmail.com"
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

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """chekcing if User have attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

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

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'NO FILE')
    def test_save_User(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
