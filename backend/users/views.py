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
def all(user_id):
    pass

# find profiles by query
@profile.route('/search', methods=['GET', 'POST'], strict_slashes=False)
@required_token
def search(user_id):
    pass

# get profile by id
@profile.route('/me', methods=['GET'], strict_slashes=False)
@required_token
def me(user_id):
    pass

# update profile by id
@profile.route('/update-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_me(user_id):
    pass

# update profile password by id
@profile.route('/update-password-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_password_me(user_id):
    pass

# update profile avatar by id
@profile.route('/update-avatar-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_avatar_me(user_id):
    pass

# update profile status by id
@profile.route('/update-status-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_status_me(user_id):
    pass

# 2FA enable
@profile.route('/2fa-enable', methods=['PUT'], strict_slashes=False)
@required_token
def two_factor_enable(user_id):
    pass

# number of profiles
@profile.route('/number-profiles', methods=['GET'], strict_slashes=False)
@required_token
def number_profiles(user_id):
    pass
