#!/usr/bin/env python3
"""MongoDB model base for backend"""
from .mongo import MongoConfig

from bson import ObjectId

from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict, List


BaseModel = {
    '_id': '',
    'created_at': '',
    'updated_at': '',
}



class Base:

    database = MongoConfig.database

    @abstractmethod
    def create(self, data: Dict) -> Dict:
        """ Create instance """
        pass

    @abstractmethod
    def all(self) -> List[Dict]:
        """ List all instance of models """
        pass
    
    @abstractmethod
    def find(self, data: Dict) -> List[Dict]:
        """ List all instance with the dict attribute """
        pass

    @abstractmethod
    def get(self, id: str) -> Dict:
        """ Get instance model by id """
        pass

    @abstractmethod
    def update(self, id: str, data: Dict) -> Dict:
        """ Update models instance """
        pass

    @abstractmethod
    def count(self) -> int:
        """ Count qll instance for models """
        pass
