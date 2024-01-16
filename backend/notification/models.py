#!/usr/bin/env python3
"""friendship conversation models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


notif = {
    'ref': '',
    'des': [],
    'type': '',
    'content': '',
    'status': '', # urgent, normal, warning, info, success, danger, 
} | BaseModel

read = {
    'user_id': '',
    'notif_id': ''
}



class Notifications(Base):
    """Notifications"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in notif.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                notif[key] = value

        notif['_id'] = str(ObjectId())
        notif['created_at'] = notif['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(notif)
        return self.collection.find_one({'_id': act.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str) -> Dict:
            
        for key, value in data.items():
            if key not in notif.keys():
                raise KeyError(f"Invalid key: {key}")
            
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'friend_id'):
            raise KeyError(f"Invalid key: {key}")
            
        notif = self.collection.find_one({'_id': id})
        if not notif:
            raise KeyError(f"Invalid id: {id}")
            
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})



class Reads(Base):
    """Reads"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in read.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                read[key] = value

        read['_id'] = str(ObjectId())
        read['created_at'] = read['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(read)
        return self.collection.find_one({'_id': act.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str) -> Dict:
            
        for key, value in data.items():
            if key not in read.keys():
                raise KeyError(f"Invalid key: {key}")
            
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'friend_id'):
            raise KeyError(f"Invalid key: {key}")
            
        read = self.collection.find_one({'_id': id})
        if not read:
            raise KeyError(f"Invalid id: {id}")
            
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})


Notifications = Notifications()
Reads = Reads()
