#!/usr/bin/python3
""" Unit test module for State class"""
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """ Unit test for State model"""

    @classmethod
    def setUpClass(cls):
        """setup for test"""
        cls.state = State()
        cls.state.name = "Arizona"

    @classmethod
    def teardown(cls):
        """removes instance at the end of the test """
        del cls.state

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_name3(self):
        """ test for state name attr type"""
        self.assertEqual(type(self.state.name), str)


if __name__ == "__main__":
    unittest.main()
