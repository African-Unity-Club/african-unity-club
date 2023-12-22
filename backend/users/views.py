#!/usr/bin/env python3
""" profile API RESTful endpoints """
from flask import Blueprint, request, jsonify

from .models import User

from ..utils.required import required_token


profile = Blueprint('profile', __name__, url_prefix='/profile')



def create_user(username, email, password):

    try:
        return User.create(
            {
                'username': username,
                'email': email,
                'password': password
            }
        )
    except Exception as e:
        return None


# get all profiles
@profile.route('/all', methods=['GET'], strict_slashes=False)
@required_token
def all(sync):
    user = User.get(sync['user_id'])
    if user and user['role'] in ('agent', 'controler', 'manager', 'admin', 'superadmin'):
        return jsonify(
            {
                'message': 'Success',
                'data': User.all()
            }
        )
    
    else:
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }
        )

# find profiles by query
@profile.route('/search', methods=['GET', 'POST'], strict_slashes=False)
@required_token
def search(sync):

    data = rquest.get_json()
    if not data:
        abort(404)
    
    return jsonify(
        {
            'message': 'Success',
            'data': User.find(data)
        }
    )

# get profile by id
@profile.route('/me', methods=['GET'], strict_slashes=False)
@required_token
def me(sync):
    
    return jsonify(
        {
            'message': 'Success',
            'data': User.get(sync['user_id'])
        }
    )

# update profile by id
@profile.route('/update-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_me(sync):
    
    data = request.get_json()
    if not data:
        abort(404)
    
    User.update(sync['user_id'], data)
    return jsonify(
        {
            'message': 'Success',
            'data': {}
        }
    )


# update profile password by id
@profile.route('/update-password-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_password_me(sync):
    pass

# update profile avatar by id
@profile.route('/update-avatar-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_avatar_me(sync):
    pass

# update profile status by id
@profile.route('/update-status-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_status_me(sync):
    pass

# 2FA enable
@profile.route('/2fa-enable', methods=['PUT'], strict_slashes=False)
@required_token
def two_factor_enable(sync):
    pass

# number of profiles
@profile.route('/number-profiles', methods=['GET'], strict_slashes=False)
@required_token
def number_profiles(sync):
    pass
