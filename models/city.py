#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """The city class, contains state ID and name

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name: The name of the City.
        state_id: The state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
