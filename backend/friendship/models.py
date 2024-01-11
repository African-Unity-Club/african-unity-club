#!/usr/bin/env python3
"""friendship conversation models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


friend = {
    'user_id': '',
    'friend_id': '',
    'status': '', # pending, accepted, blocked, rejected
} | BaseModel


follower = {
    'user_id': '',
    'follower_id': ''
}

following = {
    'user_id': '',
    'following_id': ''
}



class Friends(Base):
    """Friends"""

    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in friend.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                friend[key] = value

        friend['_id'] = str(ObjectId())
        friend['created_at'] = friend['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(friend)
        return self.collection.find_one({'_id': act.inserted_id})

    def update(self, id: str, data: Dict, user_id: str) -> Dict:
        
        for key, value in data.items():
            if key not in friend.keys():
                raise KeyError(f"Invalid key: {key}")
        
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'friend_id'):
            raise KeyError(f"Invalid key: {key}")
        
        friend = self.collection.find_one({'_id': id})
        if not friend:
            raise KeyError(f"Invalid id: {id}")
        
        if friend['user_id'] != user_id:
            raise KeyError(f"Invalid user_id: {user_id}")
        
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})



class Followers(Base):
    """Followers"""

    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in follower.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                follower[key] = value

        follower['_id'] = str(ObjectId())
        follower['created_at'] = follower['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(follower)
        return self.collection.find_one({'_id': act.inserted_id})

    def update(self, id: str, data: Dict, user_id: str) -> Dict:
        
        for key, value in data.items():
            if key not in follower.keys():
                raise KeyError(f"Invalid key: {key}")
        
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'follower_id'):
            raise KeyError(f"Invalid key: {key}")
        
        follower = self.collection.find_one({'_id': id})
        if not follower:
            raise KeyError(f"Invalid id: {id}")
        
        if follower['user_id'] != user_id:
            raise KeyError(f"Invalid user_id: {user_id}")
        
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})
    


class Followings(Base):
    """Followings"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in following.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                following[key] = value

        following['_id'] = str(ObjectId())
        following['created_at'] = following['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(following)
        return self.collection.find_one({'_id': act.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str) -> Dict:
                
        for key, value in data.items():
            if key not in following.keys():
                raise KeyError(f"Invalid key: {key}")
                
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'following_id'):
            raise KeyError(f"Invalid key: {key}")
                
        following = self.collection.find_one({'_id': id})
        if not following:
            raise KeyError(f"Invalid id: {id}")
                
        if following['user_id'] != user_id:
            raise KeyError(f"Invalid user_id: {user_id}")
                
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})
