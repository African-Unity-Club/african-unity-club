#!/usr/bin/env python3
"""MongoDB model base for backend"""
from .mongo import MongoConfig

from bson import ObjectId

from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict, List

import pymongo


BaseModel = {
    '_id': '',
    'created_at': '',
    'updated_at': '',
}



class Base:

    database = MongoConfig.database
    collection: pymongo.collection.Collection

    def __init__(self):
        self.collection = self.database[self.__class__.__name__]

    @abstractmethod
    def create(self, data: Dict) -> Dict:
        """ Create instance """
        pass

    def all(self) -> List[Dict]:
        """ List all instance of models """
        return list(self.collection.find())

    def find(self, data: Dict) -> List[Dict]:
        """ List all instance with the dict attribute """
        return list(self.collection.find(data))

    def get(self, id: str, **kwargs: Dict) -> Dict:
        """ Get instance model by id """
        kwargs['_id'] = id
        return self.collection.find_one(kwargs)

    @abstractmethod
    def update(self, id: str, data: Dict, **kwargs: Dict) -> None:
        """ Update models instance """
        pass

    def count(self) -> int:
        """ Count qll instance for models """
        return self.collection.count_documents({})

    def delete(self, id: str, **kwargs) -> None:
        kwargs['_id'] = id
        self.collection.delete_one(kwargs)
