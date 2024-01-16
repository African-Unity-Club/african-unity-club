#!/usr/bin/env python3
"""job alert models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


alert = {
    "user_id": "",
    "domain": "",
    "country": [],
    "title": "",
    "contract": [],
} | BaseModel


job = {
    "title": "",
    "description": "",
    "domain": "",
    "country": "",
    "contract": "", # CDD, CDI, Stage, Alternance, Intérim
    "company": "",
    "skills": [],
    # remote, part-time, full-time
    "type": "",
    "salary": "",
    "location": "",
} | BaseModel




class Jobs(Base):
    """Job"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in job.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                job[key] = value
        
        job['_id'] = str(ObjectId())
        job['created_at'] = job['updated_at'] = datetime.utcnow().isoformat()

        act = self.collection.insert_one(job)
        return self.collection.find_one({'_id': act.inserted_id})

    def update(self, id: str, data: Dict, user_id: str) -> Dict:
        for key, value in data.items():
            if key not in job.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key in ('_id', 'created_at', 'updated_at'):
                del data[key]

        data['updated_at'] = datetime.utcnow().isoformat()

        act = self.collection.update_one({'_id': id, 'user_id': user_id}, {'$set': data})
        return self.collection.find_one({'_id': id, 'user_id': user_id})




class Alerts(Base):
    """Job alerts"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in alert.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                alert[key] = value
        
        alert['_id'] = str(ObjectId())
        alert['created_at'] = alert['updated_at'] = datetime.utcnow().isoformat()

        act = self.collection.insert_one(alert)
        return self.collection.find_one({'_id': act.inserted_id})

    def update(self, id: str, data: Dict, user_id: str) -> Dict:
        for key, value in data.items():
            if key not in alert.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key in ('_id', 'created_at', 'updated_at'):
                del data[key]

        data['updated_at'] = datetime.utcnow().isoformat()

        act = self.collection.update_one({'_id': id, 'user_id': user_id}, {'$set': data})
        return self.collection.find_one({'_id': id, 'user_id': user_id})



Jobs = Jobs()
Alerts = Alerts()
