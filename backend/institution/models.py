#!/usr/bin/env python3
""" intitution models """
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


# tout les information pouvant identifier une institution
inst = {
    'name': '',
    'email': '',
    'owner': '',
    'admin': [],
    'phone': '',
    'country': '',
    'state': '',
    'city': '',
    'zip': '',
    'address': '',
    'website': '',
    # type d'institution
    'sector': '',
    # annee de creation
    'since': '',
    'avatar': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
} | BaseModel

attrs = inst



class Institution(Base):
    """Institution
    ==============="""

    def create(self, data: Dict):
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()

        inst = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': inst.inserted_id})
    
    def update(self, user: str, id, data: Dict):
        pass


Institution = Institution()
