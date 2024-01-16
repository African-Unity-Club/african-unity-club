#!/usr/bin/env python3
"""friendship conversation models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


task = {
    # definis tout les champ necessaire pour la creation d'une tache planifier
    'title': '',
    'description': '',
    'start': '', # yyyy-mm-dd
    'end': '', # yyyy-mm-dd
    'status': '', # pending, running, done, failed, canceled,
    'owner': '',
    'ask': [],
    'priority': '', # low, medium, high, urgent
    'type': '', # live, event, appointment, reminder,
    'location': '',
    'frequency': '', # once, daily, weekly, monthly, yearly
    'planning': [], # [ids]
    
} | BaseModel


stamp = {
    'task_id': '',
    'start_time': '', # hh:mm
    'end_time': '', # hh:mm
    'days': '', # yyyy-mm-dd
    'count': ''
} | BaseModel


session = {
    'title': '',
    'description': '',
    'start': '', # hh:mm:ss
    'end': '', # hh:mm:ss
    'days': '', # yyyy-mm-dd
    'owner': '',
    'guests': [],
    'status': '', # pending, running, done, failed, canceled,
    'ref': ''
} | BaseModel



class Tasks(Base):
    """Tasks"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in task.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                task[key] = value

        task['_id'] = str(ObjectId())
        task['created_at'] = task['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(task)
        return self.collection.find_one({'_id': act.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str) -> Dict:
            
        for key, value in data.items():
            if key not in task.keys():
                raise KeyError(f"Invalid key: {key}")
            
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'friend_id'):
            raise KeyError(f"Invalid key: {key}")
            
        task = self.collection.find_one({'_id': id})
        if not task:
            raise KeyError(f"Invalid id: {id}")
            
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})



class TimeStamp(Base):
    """TimeStamp"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in stamp.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                stamp[key] = value

        stamp['_id'] = str(ObjectId())
        stamp['created_at'] = stamp['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(stamp)
        return self.collection.find_one({'_id': act.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str) -> Dict:
            
        for key, value in data.items():
            if key not in stamp.keys():
                raise KeyError(f"Invalid key: {key}")
            
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'friend_id'):
            raise KeyError(f"Invalid key: {key}")
            
        stamp = self.collection.find_one({'_id': id})
        if not stamp:
            raise KeyError(f"Invalid id: {id}")
            
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})


class LiveSession(Base):
    """LiveSession"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in session.keys():
                raise KeyError(f"Invalid key: {key}")

            if key not in ('_id', 'created_at', 'updated_at'):
                session[key] = value

        session['_id'] = str(ObjectId())
        session['created_at'] = session['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.insert_one(session)
        return self.collection.find_one({'_id': act.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str) -> Dict:
            
        for key, value in data.items():
            if key not in session.keys():
                raise KeyError(f"Invalid key: {key}")
            
        if key in ('_id', 'created_at', 'updated_at', 'user_id', 'friend_id'):
            raise KeyError(f"Invalid key: {key}")
            
        session = self.collection.find_one({'_id': id})
        if not session:
            raise KeyError(f"Invalid id: {id}")
            
        self.collection.update_one({'_id': id}, {'$set': data})
        return self.collection.find_one({'_id': id})



Tasks = Tasks()
TimeStamp = TimeStamp()
LiveSession = LiveSession()
