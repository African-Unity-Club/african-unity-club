#!/usr/bin/env python3
""" like, share, repost and comment models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


action = {
    "user_id": "",
    "post_id": "",
    "comment": "",
    "action": "", # like, share, repost, comment
} | BaseModel


attrs = action


class Actions(Base):
    """Like, Repost, Share and Comment"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        if 'action' is 'comment' and not data['comment']:
            raise KeyError(f"Comment is required")

        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()

        act = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': act.inserted_id})

    def update(self, id: str, data: Dict, user_id: str) -> Dict:
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key in ('_id', 'created_at', 'updated_at', 'user_id', 'post_id', 'action'):
                del data[key]

        if 'action' not in ('comment', 'repost'):
            raise KeyError(f"Comment is required")

        data['updated_at'] = datetime.utcnow().isoformat()

        act = self.collection.update_one({'_id': id, 'user_id': user_id}, {'$set': data})
        return self.collection.find_one({'_id': id, 'user_id': user_id})

Actions = Actions()
