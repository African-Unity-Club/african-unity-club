#!/usr/bin/env python3
"""chat conversation models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


conv : {
    'sender': '',
    'receiver': '',
    'content': '',
    # l'endroit d'ou le message viens
    'zone': '', # direct, group, channel
    # type de message
    'topic': '', # text, image, video, audio, file, location, contact, call
    'reply_to': '', # message_id
    'marked': False, # starred, pinned
} | BaseModel


action = {
    'user_id': '',
    'ref': '',
    'action': False,
    'status': '' # archive, trash, trash_all, read, favorite
} | BaseModel





class Chats(Base):
    """Chats"""

    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in conv.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                conv[key] = value

        conv['_id'] = str(ObjectId())
        conv['created_at'] = conv['updated_at'] = datetime.utcnow().isoformat()
        conv['area'] = 'outbox'
        act = self.collection.insert_one(conv)
        return self.collection.find_one({'_id': act.inserted_id})

    def update(self, id: str, data: Dict, user_id: str) -> Dict:
        
        for key, value in data.items():
            if key not in conv.keys():
                raise KeyError(f"Invalid key: {key}")
        
        if key in ('_id', 'created_at', 'updated_at', 'sender', 'receiver', 'content', 'zone'):
            raise KeyError(f"Invalid key: {key}")
        
        data['updated'] = datetime.utcnow().isoformat()
        
        self.collection.update_one({'_id': id}, {'$set': data})
        
        return True



class MAction(Base):
    """ archive, trash, trash all, read, favorite"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in action.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                action[key] = value

        action['_id'] = str(ObjectId())
        action['created_at'] = action['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(action)
        return self.collection.find_one({'_id': act.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str) -> Dict:
            
            for key, value in data.items():
                if key not in action.keys():
                    raise KeyError(f"Invalid key: {key}")
            
            if key in ('_id', 'created_at', 'updated_at', 'user_id', 'ref'):
                raise KeyError(f"Invalid key: {key}")
            
            data['updated'] = datetime.utcnow().isoformat()
            
            self.collection.update_one({'_id': id}, {'$set': data})
            
            return True


Chats = Chats()
MAction = MAction()
