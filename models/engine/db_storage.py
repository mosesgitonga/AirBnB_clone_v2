#!/usr/bin/python3
"""Database storage switch"""
from sqlalchemy import create_engine, MetaData
from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session


name_and_class = {
    'User':User,
    'State': State,
    'City': City
}

class DBStorage:
    """db data storage"""
    __engine = None
    __session = None

    def __init__(self):
        db = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        password = getenv('HBNB_MYSQL_PWD')
        user = getenv('HBNB_MYSQL_USER')

        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}", pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns all a key and val"""
        if not self.__session:
            self.reload()

        objects = {}
        if type(cls) == str:
            cls = name_and_class.get(cls, None)

        if cls:
            for obj in self.__session.query(cls):
                objects[type(obj).__name__ + '.' + obj.id] = obj
        else:
            for cls in name_and_class.values():
                for obj in self.__session.query(cls):
                    objects[type(obj).__name__ + '.' + obj.id] = obj
        return objects

    def new(self, obj):
        """adds new obj """
        self.__session.add(obj)

    def save(self):
        """commits changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes objects"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads the databse"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()


    def close(self):
        """
        close session
        """
        self.__session.close()

        
    
