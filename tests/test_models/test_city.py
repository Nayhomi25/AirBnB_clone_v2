#!/usr/bin/python3
""" unit test module for City Model"""
import os
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ test cases for the User model """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "City"
        cls.city.state_id = "932423"

    @classmethod
    def teardown(cls):
        """removes instance at the end of the test """
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_state_id(self):
        """ test for state_id attr type"""
        self.assertEqual(type(self.city.state_id), str)

    def test_name(self):
        """ test for name sttr type"""
        self.assertEqual(type(self.city.name), str)


if __name__ == "__main__":
    unittest.main()
