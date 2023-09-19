#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from os import getenv

class DBStorage:
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
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload():
        Base.MetaData.create_all
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()
