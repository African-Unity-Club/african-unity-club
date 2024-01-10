#!/usr/bin/env python3
"""community models"""
from ..utils.mongo import MongoConfig
from ..utils.base import BaseModel, Base

from bson import ObjectId
import pymongo

from users.models import User

from typing import Dict
from datetime import datetime


cmty : {
    "name": "",
    "description": "",
    "domain": "",
    "owner": "",
    "members": [],
    "admins": [],
    "moderators": [],
    "managers": [],
    "avatar": "",
    "cover": "",
    "country": "",
    "state": "",
    "city": "",
    "address": "",
    "status": "", # active, verified, blocked, deleted, pending
    "visibility": "", # public, private, secret
    "groups": [],
} | BaseModel




class Community(Base):
    """Community"""
    
    def create(self, data: Dict) -> Dict:
        for key, value in data.items():
            if key not in cmty.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key not in ('_id', 'created_at', 'updated_at'):
                cmty[key] = value
        
        cmty['members'] = [cmty['owner']]
        cmty['admins'] = [cmty['owner']]
        cmty['status'] = 'pending'
        cmty['visibility'] = 'public'
        cmty['_id'] = str(ObjectId())
        cmty['created_at'] = cmty['updated_at'] = datetime.utcnow().isoformat()

        act = self.collection.insert_one(cmty)
        return self.collection.find_one({'_id': act.inserted_id})

    def update(self, id: str, data: Dict, user_id: str) -> Dict:
        for key, value in data.items():
            if key not in cmty.keys():
                raise KeyError(f"Invalid key: {key}")
            
            if key in ('_id', 'created_at', 'updated_at', 'owner', 'members', 'admins', 'moderators', 'managers', 'groups', 'status', 'visibility', 'avatar', 'cover'):
                cmty[key] = value
        
        cmty['updated_at'] = datetime.utcnow().isoformat()
        act = self.collection.update_one({'_id': id}, {'$set': cmty})
        return self.collection.find_one({'_id': id})
    
    def ownership(self, cm_id, owner_id):
        
        new_owner = User.get(owner_id)
        if new_owner:
            cmt = self.get(cm_id)
            if cmt['owner'] == owner_id:
                raise KeyError(f"Invalid key: {owner_id}")
            
            if owner_id not in cmt['admins'] or owner_id not in cmt['moderators'] or owner_id not in cmt['managers']:
                raise KeyError(f"Invalid key: {owner_id}")
            
            self.collection.update_one({'_id': cm_id}, {'$set': {'owner': owner_id}})
            return True
        return False
    
    def add_member(self, cm_id, member_id):
        
        new_member = User.get(member_id)
        if new_member:
            cmt = self.get(cm_id)
            if member_id not in cmt['members']:
                self.collection.update_one({'_id': cm_id}, {'$push': {'members': member_id}})
            return True
        return False
    
    def add_admin(self, cm_id, admin_id):
        
        admin = User.get(admin_id)
        if admin:
            cmt = self.get(cm_id)
            if admin_id not in cmt['moderators']:
                raise KeyError(f"Invalid key: {admin_id}")
            
            self.collection.update_one({'_id': cm_id}, {'$push': {'admins': admin_id}})
            return True
        return False
    
    def add_moderator(self, cm_id, moderator_id):
            
        moderator = User.get(moderator_id)
        if moderator:
            cmt = self.get(cm_id)
            if moderator_id not in cmt['managers']:
                raise KeyError(f"Invalid key: {moderator_id}")
            
            self.collection.update_one({'_id': cm_id}, {'$push': {'moderators': moderator_id}})
            return True
        return False
    
    def add_managers(self, cm_id, manager_id):
                
        manager = User.get(manager_id)
        if manager:
            cmt = self.get(cm_id)
            if manager_id not in cmt['members']:
                raise KeyError(f"Invalid key: {manager_id}")
            
            self.collection.update_one({'_id': cm_id}, {'$push': {'managers': manager_id}})
            return True
        return False

    def update_avatar(self, id: str, avatar: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$set': {'avatar': avatar}})
        return True

    def update_cover(self, id: str, cover: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$set': {'cover': cover}})
        return True

    def change_visibility(self, id: str, visibility: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$set': {'visibility': visibility}})
        return True

    def create_group(self, id: str, group: Dict, user_id: str) -> Dict:
        group = self.create(group)
        self.collection.update_one({'_id': id}, {'$push': {'groups': group['_id']}})
        return group
    
    def add_group(self, id: str, group_id: str, user_id: str) -> Dict:
        group = self.get(group_id)
        if group:
            self.collection.update_one({'_id': id}, {'$push': {'groups': group['_id']}})
            return group
        return None
    
    def remove_member(self, id: str, member_id: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$pull': {'members': member_id}})
        return True

    def remove_admin(self, id: str, admin_id: str, user_id: str) -> Dict:
        
        cmt = self.get(id)
        if admin_id == cmt['owner']:
            raise KeyError(f"Invalid key: {admin_id}")
        
        self.collection.update_one({'_id': id}, {'$pull': {'admins': admin_id}})
        return True

    def remove_moderator(self, id: str, moderator_id: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$pull': {'moderators': moderator_id}})
        return True
    
    def remove_manager(self, id: str, manager_id: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$pull': {'managers': manager_id}})
        return True
    
    def remove_group(self, id: str, group_id: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$pull': {'groups': group_id}})
        return True
    
    def remove_avatar(self, id: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$unset': {'avatar': 'default_avatar.png'}})
        return True
    
    def remove_cover(self, id: str, user_id: str) -> Dict:
        self.collection.update_one({'_id': id}, {'$unset': {'cover': 'default_cover.png'}})
        return True


Community = Community()
