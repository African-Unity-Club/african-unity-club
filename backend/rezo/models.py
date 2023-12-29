#!/usr/bin/env python3
"""reseaux models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from typing import Dict


reseau = {
    "name": "", # facebook, twitter, instagram, linkedin, github, gitlab, youtube, pinterest, tiktok, whatsapp, telegram, slack, discord, medium, reddit, quora, stackoverflow, behance, dribbble, spotify
    "logo": "",
    "url": "",
    "user_id": "",
} | BaseModel


attrs = reseau


class Reseaux(Base):
    """
    """

    def create(self, data: Dict):
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        attrs['logo'] = data['logo'] + '.png'
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()

        reseau = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': reseau.inserted_id})
    
    def update(self, id: str, data: Dict, user_id: str):
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at', 'user_id', 'logo', 'name'):
                attrs[key] = value
        
        attrs['updated_at'] = datetime.utcnow().isoformat()

        reseau = self.collection.update_one({'_id': id, 'user_id': user_id}, {'$set': attrs})
        return self.collection.find_one({'_id': id, 'user_id': user_id})
        

Reseaux = Reseaux()
