#!/usr/bin/python3
""" State Module for HBNB project """
import models
import shlex
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Returns the list of City instances with state_id
        equals to the current State.id
        """
        var = models.storage.all()
        tmp = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                tmp.append(var[key])
        for elem in tmp:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
