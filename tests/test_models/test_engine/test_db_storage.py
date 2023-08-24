#!/usr/bin/python3
"""test for db storage module"""
import unittest
import json
import os
import MySQLdb
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
class TestDBStorage(unittest.TestCase):
    """Class to test the db storage model"""

    @classmethod
    def setUpClass(self):
        """set up for test"""
        self.User = os.getenv("HBNB_MYSQL_USER")
        self.Passwd = os.getenv("HBNB_MYSQL_PWD")
        self.Db = os.getenv("HBNB_MYSQL_DB")
        self.Host = os.getenv("HBNB_MYSQL_HOST")
        self.db = MySQLdb.connect(host=self.Host, user=self.User,
                                  passwd=self.Passwd, db=self.Db,
                                  charset="utf8")
        self.query = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def teardown(self):
        """tear down at the end"""
        self.query.close()
        self.db.close()

    def test_attributes(self):
        """Check for attributes."""
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    def test_read_tables(self):
        """test for read tables"""
        self.query.execute("SHOW TABLES")
        tables = self.query.fetchall()
        self.assertEqual(len(tables), 7)

    def test_no_element_user(self):
        """test for no elements in users"""
        self.query.execute("SELECT * FROM users")
        users = self.query.fetchall()
        self.assertEqual(len(users), 0)

    def test_no_element_cities(self):
        """test for no elements in cities"""
        self.query.execute("SELECT * FROM cities")
        cities = self.query.fetchall()
        self.assertEqual(len(cities), 0)

    def test_add(self):
        """Test same size between storage() and existing db"""
        self.query.execute("SELECT * FROM states")
        states = self.query.fetchall()
        self.assertEqual(len(states), 0)
        state = State(name="Texas")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        states = self.query.fetchall()
        self.assertEqual(len(states), 1)


if __name__ == "__main__":
    unittest.main()
