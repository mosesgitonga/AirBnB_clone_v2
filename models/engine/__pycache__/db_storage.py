#!/usr/bin/python3
"""Database storage switch"""
from sqlalchemy import create_engine, MetaData
from os import getenv


class DBStorage:
    """db data storage"""
    __engine = None
    __session = None

    models = {User, State, City, Amenity, Place, Review}
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
        db_dict = {}
        models = self.models
        if cls:
            models = {cls}

        for model in models:
            objects = self.__session(eval(model)).all()
            for obj in objects.items():
                
                key = f"{obj.__class__.__name__}.{obj.id}"
                db_dict[key] = obj

        return db_dict
    
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

    def reload():
        """reloads the databse"""

        Base.MetaData.create_all
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()
