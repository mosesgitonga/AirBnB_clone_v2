#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', back_populates='state')
    else:
        @property
        def cities(self):
            """cities"""
            from models import storage
            cities_in_state = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
