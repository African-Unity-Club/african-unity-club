#!/usr/bin/env python3
""" awards models """
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict


award = {
    'name': '',
    'year': '',
    'institution': '',
    'user_id': ''
} | BaseModel


attrs = award


class Awards(Base):
    """ Award """

    def create(self, data: Dict):
        for key in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()

        award = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': award.inserted_id})
    
    def update(self, user: str, id, data: Dict):

        for key in data.keys():
            if key not in ('name', 'year', 'institution'):
                raise KeyError(f"Invalid key: {key}")
        
        data['updated_at'] = datetime.utcnow().isoformat()
        return self.collection.update_one({'_id': id, 'user_id': user}, {'$set: data'})



Awards = Awards()
