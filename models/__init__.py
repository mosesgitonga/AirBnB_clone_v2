#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.base_model import BaseModel, Base
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
storage.reload() 
