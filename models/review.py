#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv



class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        text = Column(String(128), nullable=False)
        place_id = Column(String(128), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
