#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (String): The amenity name.
        place_amenities (relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
