#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (String): The review description.
        place_id (String): The review's place id.
        user_id ( String): The review's user id.
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
