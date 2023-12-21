#!/usr/bin/env python3
""" profile API RESTful endpoints """
from flask import Blueprint, request, jsonify

from .models import User


profile = Blueprint('profile', __name__, url_prefix='/profile')



def create_user(username, email, password, **kwargs):

    try:
        kwargs['username'] = username
        kwargs['email'] = email
        kwargs['password'] = password
        
        return User.create(kwargs)
    except Exception as e:
        return None


# get all profiles
@profile.route('/all', methods=['GET'], strict_slashes=False)
def all():
    pass

# find profiles by query
@profile.route('/search', methods=['GET', 'POST'], strict_slashes=False)
def search():
    pass

# get profile by id
@profile.route('/me', methods=['GET'], strict_slashes=False)
def me():
    pass

# update profile by id
@profile.route('/update-me', methods=['PUT'], strict_slashes=False)
def update_me():
    pass

# update profile password by id
@profile.route('/update-password-me', methods=['PUT'], strict_slashes=False)
def update_password_me():
    pass

# update profile avatar by id
@profile.route('/update-avatar-me', methods=['PUT'], strict_slashes=False)
def update_avatar_me():
    pass

# update profile status by id
@profile.route('/update-status-me', methods=['PUT'], strict_slashes=False)
def update_status_me():
    pass

# number of profiles
@profile.route('/number-profiles', methods=['GET'], strict_slashes=False)
def number_profiles():
    pass
