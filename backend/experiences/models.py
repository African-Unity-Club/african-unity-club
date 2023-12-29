#!/usr/bin/env python3
"""experiences models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from institutions.models import Institutions

from bson import ObjectId
import pymongo

from typing import Dict


experience = {
    "name": "",
    "institution": "",
    "description": "",
    "user_id": "",
    "start": "",
    "end": "",
    "level": "", # [DNB/BEPC], [HSD/BAC], [BAC+2/DUT/DEUG/A.A/A.S], [Licence/B.A/B.S], [Master/M.A/M.S/MBA], [Ph.D/Doctorat], [Post-Doctorat]
    "type": "", # diplome, certificat, formation, stage, experience
} | BaseModel

attrs = experience



class Experiences(Base):
    """
    """

    def create(self, data: Dict):
        for key, value in data.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                attrs[key] = value
        
        institution = Institutions().get(data['institution'])
        if institution:
            attrs['institution'] = {
                'name': institution['name'],
                'avatar': institution['avatar']
            }
        else:
            attrs['institution'] = {
                'name': attrs['institution'],
                'avatar': ''
            }

        attrs['start'] = datetime.strptime(attrs['start'], '%Y-%m-%d').strftime('%Y-%m-%d')
        attrs['end'] = datetime.strptime(attrs['end'], '%Y-%m-%d').strftime('%Y-%m-%d')
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()

        experience = self.collection.insert_one(attrs)
        return self.collection.find_one({'_id': experience.inserted_id})
    
    def update(self, id: str, data: Dict, user: str):

        for key in data.keys():
            if key not in ('name', 'institution', 'description', 'start', 'end'):
                raise KeyError(f"Invalid key: {key}")
        
        institution = Institutions().get(data['institution'])
        data['updated_at'] = datetime.utcnow().isoformat()
        data['start'] = datetime.strptime(data.get('start', institution['start']), '%Y-%m-%d').strftime('%Y-%m-%d')
        data['end'] = datetime.strptime(data.get('end', institution['end']), '%Y-%m-%d').strftime('%Y-%m-%d')
        return self.collection.update_one({'_id': id, 'user_id': user}, {'$set: data'})


Experiences = Experiences()
