#!/usr/bin/env python3
"""MongoDB database for profile"""
from ..utils.mongo import MongoConfig
from ..utils.common import IMAGES_UPLOAD_FOLDER as UPLOAD_FOLDER
from ..utils.base import BaseModel, Base

from bson import ObjectId
from dotenv import load_dotenv
import pymongo

from datetime import datetime
from typing import Dict, List

import os


load_dotenv()


ProfileModel = {
    'username': '',
    'password': '',
    'first_name': '',
    'last_name': '',
    'birth': '',
    'email': '',
    'phone': '',
    'avatar': os.path.join(UPLOAD_FOLDER, 'nouser.png'),
    'country': '',
    'state': '',
    'city': '',
    'street': '',
    'about': '',
    'role': 'user', # user, agent, controler, manager, admin, superadmin
    'last_login': '',
    'status': 'pending', # pending, active, inactive, blocked, deleted
} | BaseModel

attrs = ProfileModel




class User(Base):

    """
    User Model
    ==========
    + _id
    + created_at
    + updated_at
    + username
    + password
    + first_name
    + last_name
    + birth
    + email
    + phone
    + avatar
    + country
    + state
    + city
    + street
    + about
    + is_active
    + role
    + last_login
    + status

    example
    =======
    
    ```
    >>> user = User.create({'username': 'myname', 'password': 'mypassword'})
    >>> print(user)
    ```
    """

    def __init__(self):
        """Initialize User Model"""
        self.datatable: pymongo.collection.Collection = self.database[self.__class__.__name__]

    def create(self, user: Dict):

        for key, value in user.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at', 'role', 'status', 'last_login'):
                attrs[key] = value
        
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()
        
        user = self.datatable.insert_one(attrs)
        return self.datatable.find_one({'_id': user.inserted_id})
    
    def all(self):

        return list(self.datatable.find({}))
    
    def find(self, dict: Dict):

        return list(self.datatable.find(dict))
    
    def get(self, id: str):
        
        return self.datatable.find_one({'_id': id})
    
    def update(self, id: str, user: Dict):
        
        for key, value in user.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key in (
                '_id',
                'created_at',
                'updated_at',
                'role',
                'status',
                'last_login',
                'password',
                'avatar'
            ):
                del user[key]
        
        user['updated_at'] = datetime.utcnow().isoformat()
        
        usr = self.datatable.update_one({'_id': id}, {'$set': user})
        return self.datatable.find_one({'_id': usr.upserted_id})
    
    def update_password(self, id: str, password: str) -> Dict:
        """Update user password"""
        user = self.datatable.update_one({'_id': id}, {'$set': {'password': password}})
        return self.datatable.find_one({'_id': user.upserted_id})
    
    def update_avatar(self, id: str, avatar: str) -> Dict:
        """Update user avatar"""
        user = self.datatable.update_one({'_id': id}, {'$set': {'avatar': avatar}})
        return self.datatable.find_one({'_id': user.upserted_id})
    
    def update_role(self, id: str, role: str) -> Dict:
        """Update user role"""
        user = self.datatable.update_one({'_id': id}, {'$set': {'role': role}})
        return self.datatable.find_one({'_id': user.upserted_id})
    
    def update_status(self, id: str, status: str) -> Dict:
        """Update user status"""
        user = self.datatable.update_one({'_id': id}, {'$set': {'status': status}})
        return self.datatable.find_one({'_id': user.upserted_id})
    
    def update_last_login(self, id: str, last_login: str) -> Dict:
        """Update user last login"""
        user = self.datatable.update_one({'_id': id}, {'$set': {'last_login': last_login}})
        return self.datatable.find_one({'_id': user.upserted_id})
    
    def count(self) -> int:
        """Count all users"""
        return self.datatable.count_documents({})


User = User()
