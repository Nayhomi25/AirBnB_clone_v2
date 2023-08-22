#!/usr/bin/python3
""" unit test module for review class"""
import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ test cases for the Review model"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "Best class"

    @classmethod
    def teardown(cls):
        """removes instance at the end of the test"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_place_id(self):
        """ test for review place_id attr type"""
        self.assertEqual(type(self.rev.place_id), str)

    def test_user_id(self):
        """ test for review user_id attr type"""
        self.assertEqual(type(self.rev.user_id), str)

    def test_text(self):
        """ test for review text attr type"""
        self.assertEqual(type(self.rev.text), str)


if __name__ == "__main__":
    unittest.main()
