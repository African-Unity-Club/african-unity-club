#!/usr/bin/env python3
""" posts models """
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime



post = {
    'content': '',
    'author': '',
    'reference': '', # social, cultural, talent, history, emplois, actuality, etc
    'category': '', # personal, institution, club, etc
    # personne ou institution taguer
    'tags': [],
    # publier ou non
    'published': False,
    # date de publication
    'published_at': '',
    # image de couverture
    'cover': ''
} | BaseModel

attrs = post



class Posts(Base):
    """Posts
    ==============="""

    def create(self, data: Dict):
        for key, value in data.items():
            if key not in post.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()
        
        p = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': p.inserted_id})
    
    def update(self, _id: str, data: Dict):
        for key, value in data.items():
            if key not in post.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key in ('_id', 'created_at', 'updated_at', 'author', 'reference', 'category', 'published', 'published_at', 'tags'):
                del data[key]
        
        data['updated_at'] = datetime.utcnow().isoformat()
        
        p = self.collection.update_one({'_id': _id}, {'$set': data})
        return self.collection.find_one({'_id': _id})
    
    def publish(self, _id: str):
        p = self.collection.update_one({'_id': _id}, {'$set': {'published': True, 'published_at': datetime.utcnow().isoformat()}})
        return self.collection.find_one({'_id': _id})

    def add_tag(self, _id: str, tag: str):
        self.collection.update_one({'_id': _id}, {'$push': {'tags': tag}})
        return self.collection.find_one({'_id': _id})
    
    def remove_tag(self, _id: str, tag: str):
        self.collection.update_one({'_id': _id}, {'$pull': {'tags': tag}})
        return self.collection.find_one({'_id': _id})

Posts = Posts()
