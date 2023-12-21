#!/usr/bin/env python3
""" authentication file """
from flask import Blueprint, jsonify, request, abort
from utils.encrypt.encrypt import MPIEncryptor as Encrypt

from users.models import User
from users.views import create_user

from .jwtoken import required_token

from datetime import datetime


auth = Blueprint('auth', __name__)



# signup route
@auth.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """ signup """

    data = request.json
    if not data:
        abort(400, 'Not a JSON')
    
    username = data.get('username')
    # check if username is already exists
    if len(User.find(username=username)):
        return jsonify(
            {
                'message': 'username already exists',
                'data': {}
            }
        ), 400
    
    email = data.get('username')
    # check if email is already exists
    if len(User.find(email=email)):
        return jsonify(
            {
                'message': 'email already exists',
                'data': {}
            }
        ), 400
    
    password = data.get('password')
    # check if password is strong enough
    if len(password) < 8:
        return jsonify(
            {
                'message': 'password is too short',
                'data': {}
            }
        ), 400
    
    # otp
    
    # create user
    user = create_user(username, email, password, status='active')
    if not user:
        return jsonify(
            {
                'message': 'something went wrong',
                'data': {}
            }
        ), 400
    
    jwt_token = Encrypt.jwt.tokenizer({'user_id': user['_id']})
    User.update_last_login(user['_id'], last_login=datetime.now().isoformat())

    return jsonify(
        {
            'message': 'Success',
            'data': {
                'user': user,
                'token': jwt_token
            }
        }
    )


# signin route
@auth.route('/signin', methods=['POST'], strict_slashes=False)
def signin():
    """signin"""

    data = request.json
    if not data:
        abort(400, 'no data provided')
    
    username = data.get('username') # username or email
    password = data.get('password')

    by_username = User.find(username=username)
    by_email = User.find(email=username)

    user = by_username if len(by_username) else by_email
    if not len(user):
        return jsonify(
            {
                'message': 'user not found',
                'data': {}
            }
        ), 400
    
    if not Encrypt.pwdhash.is_verify(password, user[0]['password']):
        return jsonify(
            {
                'message': 'invalid password',
                'data': {}
            }
        ), 400
    
    token = Encrypt.jwt.tokenizer({'user_id': user[0]['_id']})
    User.update_last_login(user[0]['_id'], last_login=datetime.now().isoformat())
    User.update_status(user[0]['_id'], status='active')

    return jsonify(
        {
            'message': 'Success',
            'data': {
                'user': user[0],
                'token': token
            }
        }
    )


# signout route
@auth.route('/signout', methods=['POST'], strict_slashes=False)
@required_token
def signout(user_id):
    """signout"""

    User.update_status(user_id, status='inactive')
    User.update_last_login(user_id, last_login=datetime.now().isoformat())

    return jsonify(
        {
            'message': 'Success',
            'data': {}
        }
    )

