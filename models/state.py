#!/usr/bin/python3
"""This is the state class"""
import models
from os import getenv
from models.base_model import BaseModel
from models.city import City, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            lista = []
            """y_dict = models.storage.all(City)"""
            """return [value for key, value in city_dict.items()"""
            """ if value.state_id == self.id]"""
            """ for city in city_dict.values():"""
            """if city.state_id == self.id:"""
            """lista.append(city)"""
            """return lista"""
            for i, j in models.storage.all().items():
                if j.__class__.__name__ == 'City':
                    if j.state_id == self.id:
                        lista.append(j)
            return lista

