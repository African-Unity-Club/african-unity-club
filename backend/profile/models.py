#!/usr/bin/env python3
"""MongoDB database for profile"""
from backend.mongo import MongoConfig
from backend.common import UPLOAD_FOLDER
from backend.models import BaseModel

from bson import ObjectId
from dotenv import load_dotenv

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



class User:

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
    """

    def __init__(self):
        """Initialize User Model"""
        self.__db = MongoConfig.client['profile']
        self.__users = self.__db['users']

    def create(self, user: Dict) -> Dict:
        """Create new user"""
        for key, value in user.items():
            if key not in attrs.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at', 'role', 'status', 'last_login'):
                attrs[key] = value
        
        attrs['_id'] = str(ObjectId())
        attrs['created_at'] = attrs['updated_at'] = datetime.utcnow().isoformat()
        
        user = self.__users.insert_one(attrs)
        return self.__users.find_one({'_id': user.inserted_id})
    
    def all(self) -> List[Dict]:
        """Get all users"""
        return list(self.__users.find({}))
    
    def find(self, dict: Dict) -> List[Dict]:
        """Get user by id"""
        return list(self.__users.find_one(dict))
    
    def get(self, id: str) -> Dict:
        """Get user by id"""
        return self.__users.find_one({'_id': id})
    
    def update(self, id: str, user: Dict) -> Dict:
        """Update user"""
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
        
        usr = self.__users.update_one({'_id': id}, {'$set': user})
        return self.__users.find_one({'_id': usr.upserted_id})
    
    def update_password(self, id: str, password: str) -> Dict:
        """Update user password"""
        user = self.__users.update_one({'_id': id}, {'$set': {'password': password}})
        return self.__users.find_one({'_id': user.upserted_id})
    
    def update_avatar(self, id: str, avatar: str) -> Dict:
        """Update user avatar"""
        user = self.__users.update_one({'_id': id}, {'$set': {'avatar': avatar}})
        return self.__users.find_one({'_id': user.upserted_id})
    
    def update_role(self, id: str, role: str) -> Dict:
        """Update user role"""
        user = self.__users.update_one({'_id': id}, {'$set': {'role': role}})
        return self.__users.find_one({'_id': user.upserted_id})
    
    def update_status(self, id: str, status: str) -> Dict:
        """Update user status"""
        user = self.__users.update_one({'_id': id}, {'$set': {'status': status}})
        return self.__users.find_one({'_id': user.upserted_id})
    
    def count(self) -> int:
        """Count all users"""
        return self.__users.count_documents({})


User = User()
