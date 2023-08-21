#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os


class test_User(test_basemodel):
    """test cases for the User model """

    def __init__(self, *args, **kwargs):
        """ User test for __init__"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """testing user first_name attribute """
        new = self.value()
        self.assertEqual(type(new.first_name), str if 
                         os.getenv('HBNB_TYPE_STORAGE') !='db' else
                         type(None))

    def test_last_name(self):
        """ testing user last_name attr"""
        new = self.value()
        self.assertEqual(type(new.last_name), str if 
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_email(self):
        """ testing uer email attr"""
        new = self.value()
        self.assertEqual(type(new.email), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_password(self):
        """ testing user password attr"""
        new = self.value()
        self.assertEqual(type(new.password), str if 
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
