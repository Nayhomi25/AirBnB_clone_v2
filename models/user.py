#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        places (relationship): User-Place relationship.
        reviews (relationship): User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship('Review', backref='user',
                           cascade='all, delete, delete-orphan')
