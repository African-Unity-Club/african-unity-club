#!/usr/bin/env python3
"""skills models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId


skill = {
    '_id': '',
    'created_at': '',
    'updated_at': '',
    'name': '',
    'user_id': '',
    'jauge': ''
}

attrs = skill



class Skills(Base):
    """
    """

    def __inti__(self):
        self.collection: pymongo.collection.Collection = self.database[self.__class__.__name__]

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
    
    def all(self):
        return list(self.collection.find({}))
    
    def find(self, data: Dict):
        return list(self.collection.find(data))
    
    def get(self, user: str, id: str):
        return self.collection.find_one({'_id': id, 'user_id': user})
    
    def update(self, user: str, id, data):

        for key in data.keys():
            if key not in ('name', 'jauge'):
                raise KeyError(f"Invalid key: {key}")
        
        data['updated_at'] = datetime.utcnow().isoformat()
        return self.collection.update_one({'_id': id, 'user_id': user}, {'$set: data'})

    def count(self):
        return self.collection.count_documents({})
    
    def delete(self, user: str, id):
        return self.collection.delete_one({'_id': id, 'user_id': user})


Skills = Skills()
