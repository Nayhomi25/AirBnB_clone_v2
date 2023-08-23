#!/usr/bin/python3
"""Unit test module for place """
import unittest
import os
from models.base_model import BaseModel
from models.place import Place
import pep8


class TestPlace(unittest.TestCase):
    """test cases for the Place model"""

    @classmethod
    def setUpClass(cls):
        """setup for test"""
        cls.place = Place()
        cls.place.city_id = "1234-abcd"
        cls.place.user_id = "4321-dcba"
        cls.place.name = "Death Star"
        cls.place.description = "UNLIMITED POWER!!!!!"
        cls.place.number_rooms = 1000000
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 607360
        cls.place.price_by_night = 10
        cls.place.latitude = 160.0
        cls.place.longitude = 120.0
        cls.place.amenity_ids = ["1324-lksdjkl"]

    @classmethod
    def teardown(cls):
        """removes instance at the end of the test"""
        del cls.place

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Place(self):
        """checking for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_Place(self):
        """chekcing if amenity have attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_is_subclass_Place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_city_id(self):
        """ test for city_ids attr type"""
        self.assertEqual(type(self.place.city_id), str)

    def test_user_id(self):
        """ test for user_ids"""
        self.assertEqual(type(self.place.user_id), str)

    def test_name(self):
        """ test for name attr type"""
        self.assertEqual(type(self.place.name), str)

    def test_description(self):
        """ test for description attr type"""
        self.assertEqual(type(self.place.description), str)

    def test_number_rooms(self):
        """ test for number_rooms attr type"""
        self.assertEqual(type(self.place.number_rooms), int)

    def test_number_bathrooms(self):
        """ test for number_bathrooms attr type"""
        self.assertEqual(type(self.place.number_bathrooms), int)

    def test_max_guest(self):
        """ test for max_guest attr type"""
        self.assertEqual(type(self.place.max_guest), int)

    def test_price_by_night(self):
        """ Test for price_by_night attr type"""
        self.assertEqual(type(self.place.price_by_night), int)

    def test_latitude(self):
        """ test for latitude attr type"""
        self.assertEqual(type(self.place.latitude), float)

    def test_longitude(self):
        """ test for longitude attr type"""
        self.assertEqual(type(self.place.latitude), float)

    def test_amenity_ids(self):
        """ Test for aenity_ids attr type"""
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_save_Place(self):
        """test if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_Place(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
