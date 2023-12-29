#!/usr/bin/env python3
"""skills models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict


skill = {
    'name': '',
    'domain': '',
    'description': '',
    'user_id': '',
    'jauge': ''
} | BaseModel

attrs = skill



class Skills(Base):
    """
    """

    def create(self, data: Dict):
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()

        skill = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': skill.inserted_id})
    
    def update(self, id: str, data: Dict, user: str):

        for key in data.keys():
            if key not in ('name', 'jauge'):
                raise KeyError(f"Invalid key: {key}")
        
        data['updated_at'] = datetime.utcnow().isoformat()
        return self.collection.update_one({'_id': id, 'user_id': user}, {'$set: data'})


Skills = Skills()
