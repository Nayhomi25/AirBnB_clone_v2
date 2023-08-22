#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


place_amenity_table = Table("place_amenity", Base.metadata,
                            Column("place_id", String(60),
                                   ForeignKey("places.id"),
                                   primary_key=True,
                                   nullable=False),
                            Column("amenity_id", String(60),
                                   ForeignKey("amenities.id"),
                                   primary_key=True,
                                   nullable=False))


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        __tablename__ (str): The name of the MySQL table to store places.
        city_id (sqlalchemy String): The place's city id.
        user_id (sqlalchemy String): The place's user id.
        name (sqlalchemy String): The name.
        description (sqlalchemy String): The description.
        number_rooms (sqlalchemy Integer): The number of rooms.
        number_bathrooms (sqlalchemy Integer): The number of bathrooms.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_by_night (sqlalchemy Integer): The price by night.
        latitude (sqlalchemy Float): The place's latitude.
        longitude (sqlalchemy Float): The place's longitude.
        reviews (sqlalchemy relationship): The Place-Review relationship.
        amenities (sqlalchemy relationship): The Place-Amenity relationship.
        amenity_ids (list): An id list of all linked amenities.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False,
                             back_populates="place_amenities")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """ Returns list of amenity ids
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute
            """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
