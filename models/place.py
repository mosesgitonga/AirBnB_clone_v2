#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from os import getenv
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False)
        number_bathrooms = Column(Integer, nullable=False)
        max_guest = Column(Integer, nullable=False)
        price_by_night = Column(Integer, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ returns a list """
            rev = []
            for val in models.storage.all(Review).values():
                if val.place_id == self.id:
                    rev.append(val)
            return rev

        @property
        def amenities(self):
            """ returns the list of Amenity instances where the
            amenity id's are linked to the Place id """
            amen = []
            for val in models.storage.all(Amenity).values():
                if val.place_id == self.id:
                    amen.append(val)
            return amen

        @amenities.setter
        def amenities(self, val=None):
            """ appends all the values that match the place id from
            Amenities """
            if val is None:
                return
            else:
                for val in models.storage.all(Amenity).values():
                    if val.place_id == self.id:
                        amenity_ids.append(val)

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places_id'),
                             primary_key=True, nullable=False)
                      Column('amenity_id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))
