#!/usr/bin/env python3
""" authentication file """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
import requests

from ..utils.encrypt.encrypt import MPIEncryptor as Encrypt
from ..utils.required import required_token
from ..utils.redis import redis_client
from ..utils.encrypt.mbauth import MobileGoogleAuth

from ..users.models import User
from ..users.views import create_user

from datetime import datetime, timedelta
from typing import Dict
import os
import json



load_dotenv()

auth = Flask(__name__)

auth.config['ENV'] = os.environ.get('FLASK_ENV')
auth.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
auth.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
auth.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(auth, resources={r"/*": {"origins": "*"}})


bcrypt = Bcrypt(auth)


# gestion d'erreur
@auth.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@auth.errorhandler(401)
def unauthorized(error):
    """ unauthorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@auth.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@auth.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@auth.errorhandler(Exception)
def internal_server_error(error):
    """ internal server error """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500


# forgot password
@auth.route('/forgot-password', methods=['POST'], strict_slashes=False)
def forgot_password():
    """ forgot password """
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    email = data.get('email')
    if not email:
        abort(400, 'email is required')
    
    user = User.find({'email': email})
    if not len(user):
        return jsonify(
            {
                'message': 'user not found',
                'data': {}
            }
        ), 400
    
    user = user[0]
    # send email personnal code and link for password change
    # save code in redis with  code : user_id
    return jsonify(
        {
            'message': 'Success',
            'data': {}
        }
    ), 200


# change password
@auth.route('/change-password', methods=['POST'], strict_slashes=False)
def change_password():

    data = request.get_json()
    if not data:
        abort(404)
    
    code = data.get('code')
    user_id = redis_client.set(str(code))
    if user_id:
        password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
        User.update_password(user_id, password)
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }
        ), 200
    else:
        return jsonify(
            {
                'message': 'Error',
                'data': {}
            }
        ), 400
    


# token
@auth.route('/rtoken', methods=['POST'], strict_slashes=False)
def rtoken():
    """token"""
    data = request.get_json()
    if not data:
        abort(404)

    user_id = data.get('user_id')
    try:
        user = User.get(user_id)
        
        if not user:
            return jsonify(
                {
                    'message': 'user not found',
                    'data': {}
                }
            ), 404
        
        User.update_status(user['_id'], status='active')
        token = Encrypt.jwt.tokenizer({'user_id': user['_id']})
        print(user)
        User.update_last_login(user['_id'], last_login=datetime.now().isoformat())

        user = User.get(user['_id'])
        user['token'] = token
        
        return jsonify(
            {
                'message': 'Success',
                'data': user
            }
        ), 200
    
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': {}
            }
        ), 200


# 2fa verify route
@auth.route('/2fa-verify', methods=['POST'], strict_slashes=False)
def two_factor_verify():
    
    data = request.get_json()
    if not data:
        abort(404)
    
    user_id = data.get('user_id')

    try:
        user = User.get(user_id)
        if not user:
            return jsonify(
                {
                    'message': 'user not found',
                    'data': {}
                }
            ), 404
        
        url = 'http://127.0.0.1' + ':' + auth.config['FLASK_RUN_PORT'] + '/rtoken'
        
        # if 2fa 
        _2fa = redis_client.get(user_id + '_2fa')
        if _2fa:
            
            # vérifier le code à usage unique lors de la connexion
            if MobileGoogleAuth.verify(redis_client.get(user_id + '_2fa'), data.get('code')):
                return requests.post(url, data=json.dumps({'user_id': user_id}), headers={'Content-Type': 'application/json'}).json()
            else:
                return jsonify(
                    {
                        'message': 'Invalid code',
                        'data': {}
                    }
                ), 401
        else:
            return requests.post(url, data=json.dumps({'user_id': user_id}), headers={'Content-Type': 'application/json'}).json()

    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404


# signup route
@auth.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """ signup """

    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    username = data.get('username')
    # check if username is already exists
    if len(User.find({'username': username})):
        return jsonify(
            {
                'message': 'username already exists',
                'data': {}
            }
        ), 400
    
    email = data.get('email')
    # check if email is already exists
    if len(User.find({'email': email})):
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
    
    password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # otp

    # create user
    user = create_user(username, email, password)
    if not user:
        return jsonify(
            {
                'message': 'something went wrong',
                'data': {}
            }
        ), 400
    
    url = 'http://127.0.0.1' + ':' + auth.config['FLASK_RUN_PORT'] + '/rtoken'
    
    return requests.post(
        url,
        data=json.dumps({'user_id': user['_id']}),
        headers={'Content-Type': 'application/json'}
    ).json()



# signin route
@auth.route('/signin', methods=['POST'], strict_slashes=False)
def signin():
    """signin"""

    data = request.json
    if not data:
        abort(400, 'no data provided')
    
    username = data.get('username') # username or email
    password = data.get('password')

    by_username = User.find({'username': username})
    by_email = User.find({'email': username})

    user = by_username if len(by_username) else by_email
    if not len(user):
        return jsonify(
            {
                'message': 'user not found',
                'data': {}
            }
        ), 400
    
    
    if not bcrypt.check_password_hash(user[0]['password'], password):
        return jsonify(
            {
                'message': 'invalid password',
                'data': {}
            }
        ), 400

    user = User.get(user[0]['_id'])
    if not user:
        return jsonify(
            {
                'message': 'user not found',
                'data': {}
            }
        ), 400

    url = 'http://127.0.0.1' + ':' + auth.config['FLASK_RUN_PORT'] + '/2fa-verify'

    return requests.post(url, data=json.dumps({'user_id': user['_id']}), headers={'Content-Type': 'application/json'}).json()


# signout route
@auth.route('/signout', methods=['POST'], strict_slashes=False)
@required_token
def signout(sync):
    """signout"""

    User.update_status(sync['user_id'], status='inactive')
    User.update_last_login(sync['user_id'], last_login=datetime.now().isoformat())
    sync['exp'] = datetime.utcnow() - timedelta(minutes=5)
    
    return jsonify(
        {
            'message': 'Success',
            'data': {}
        }
    ), 200


if __name__ == '__main__':
    auth.run()

# flask --app app run --debug
