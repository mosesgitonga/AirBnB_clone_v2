#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        city = relationship('City', back_populates='state', cascade='all, delete-orpahn')

     else:
        @property
        def cities(self):
            cities_in_state = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            retuen cities_in_state
