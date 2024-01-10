#!/usr/bin/env python3
""" awards models """
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from institution.models import Institution

from bson import ObjectId
import pymongo

from typing import Dict
from datetime import datetime


award = {
    'name': '',
    'year': '',
    'description': '',
    'institution': '',
    'user_id': ''
} | BaseModel


attrs = award


class Awards(Base):
    """ Award """

    def create(self, data: Dict):
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        institution = Institution().get(data['institution'])
        if institution:
            attrs['institution'] = {
                '_id': institution.get('_id'),
                'name': institution.get('name'),
                'avatar': institution.get('avatar'),
                'country': institution.get('country')
            }
        else:
            attrs['institution'] = {
                '_id': attrs['institution'],
                'name': '',
                'avatar': '',
                'country': ''
            }
        
        attrs['year'] = datetime.strptime(attrs['year'], '%Y').strftime('%Y')
        
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()

        award = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': award.inserted_id})
    
    def update(self, user: str, id, data: Dict):

        for key in data.keys():
            if key not in ('name', 'year', 'institution'):
                raise KeyError(f"Invalid key: {key}")
        
        data['updated_at'] = datetime.utcnow().isoformat()
        self.collection.update_one({'_id': id, 'user_id': user}, {'$set: data'})



Awards = Awards()
