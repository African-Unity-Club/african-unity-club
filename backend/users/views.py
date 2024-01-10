#!/usr/bin/env python3
""" profile API RESTful endpoints """
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from dotenv import load_dotenv
import requests
from flask_bcrypt import Bcrypt

from .models import User

from ..utils.required import required_token
from ..utils.encrypt.mbauth import MobileGoogleAuth
from ..utils.redis import redis_client

from datetime import datetime, timedelta
from typing import Dict
import os


load_dotenv()

profile = Flask(__name__)

profile.config['ENV'] = os.environ.get('FLASK_ENV')
profile.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
profile.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
profile.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(profile, resources={r"/*": {"origins": "*"}})

bcrypt = Bcrypt(profile)


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


# find profiles by query
@profile.route('/users-search', methods=['POST'], strict_slashes=False)
@required_token
def search(sync):

    data = request.get_json()
    if not data:
        abort(404)
    
    try:
        users = User.find(data)
        for user in users:
            del user['password']
        return jsonify(
            {
                'message': 'Success',
                'data': users
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }
        ), 404

# get profile by id
@profile.route('/users-me', methods=['GET'], strict_slashes=False)
@required_token
def me(sync):
    
    try:
        user = User.get(sync['user_id'])
        del user['password']
        return jsonify(
            {
                'message': 'Success',
                'data': user
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': User.get(sync['user_id'])
            }
        ), 401


@profile.route('/users/<id>', methods=['GET'], strict_slashes=False)
@required_token
def user(sync, id):
    
    try:
        user = User.get(id)
        act = User.get(sync['user_id'])
        del user['password']
        if user and act['role'] in ('agent', 'controler', 'manager', 'admin', 'superadmin'):
            return jsonify(
                {
                    'message': 'Success',
                    'data': user
                }
            ), 200
        else:
            return jsonify(
                {
                    'message': 'Unauthorized',
                    'data': {}
                }
            ), 401
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404


@profile.route('/users-profile/<id>', methods=['GET'], strict_slashes=False)
@required_token
def user_profile(sync, id):

    try:
        user = User.get(id)
        profile = {
            'username': user['username'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'phone': user['phone'],
            'avatar': user['avatar'],
            'country': user['country'],
            'about': user['about']
        }
        return jsonify(
            {
                'message': 'Success',
                'data': profile
            }
        ), 200
        
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404
    


# update profile by id
@profile.route('/users-update-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_me(sync):
    
    data = request.get_json()
    if not data:
        abort(404)

    try:
    
        User.update(sync['user_id'], data)
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404


# update profile password by id
@profile.route('/users-update-password-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_password_me(sync):
    
    data = request.get_json()
    if not data:
        abort(404)
    
    try:
        user = User.get(sync['user_id'])

        verify = bcrypt.check_password_hash(user['password'], data.get('old_password'))
        if not verify:
            return jsonify(
                {
                    'message': 'Error',
                    'data': 'Passwords do not match'
                }
            ), 401

        password = bcrypt.generate_password_hash(data.get('new_password')).decode('utf-8')
        
        User.update_password(sync['user_id'], password)
        # deconnecter l'utilisateur
        url = 'http://127.0.0.1:8000/signout'
        token = request.headers.get('Authorization').split(' ')[1]
        requests.post(url, headers={'Authorization': '--AUC-- ' + token, 'Content-type': 'application/json'})
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404


# update profile avatar by id
def traitement_avatar(avatar, user_id):

    # condition sur la taille de l'image en fonction de l'abonnement
    pass


@profile.route('/users-update-avatar-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_avatar_me(sync):
    
    try:
        if not traitement_avatar(request.get_json().get('avatar'), sync['user_id']):
            return jsonify(
                {
                    'message': 'Error',
                    'data': 'Error'
                }
            ), 401
        User.update_avatar(sync['user_id'], request.get_json().get('avatar'))
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404

# update profile status by id
@profile.route('/users-update-status-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_status_me(sync):
    
    data = request.get_json()
    if not data:
        abort(404)
    try:
        User.update_status(sync['user_id'], data.get('status'))
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404


# 2FA enable
@profile.route('/2fa-enable', methods=['PUT'], strict_slashes=False)
@required_token
def two_factor_enable(sync):

    data = request.get_json()
    if not data:
        abort(404)
    
    try:
        if data.get('2fa') == False:
            return jsonify(
                {
                    'message': 'Error',
                    'data': '2FA is disabled'
                }
            ), 401
        _2fa_key = MobileGoogleAuth.keygen

        # enregistrer la clé secrète dans la base de donnée redis
        redis_client.set(sync['user_id'] + '_2fa', _2fa_key)

        # générer le code QR
        _2fa_qrcode = MobileGoogleAuth.qrcode(_2fa_key)

        # renvoyer le code QR
        return jsonify(
            {
                'message': 'Success',
                'data': {
                    'key': _2fa_key,
                    'qrcode': _2fa_qrcode
                }
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 404


# 2FA disable
@profile.route('/2fa-disable', methods=['PUT'], strict_slashes=False)
@required_token
def two_factor_disable(sync):
    
    # supprimer la clé secrète dans la base de donnée redis
    return jsonify(
        {
            'message': 'Success',
            'data': {}
        }
    ), 200


# number of profiles
@profile.route('/users-number-profiles', methods=['GET'], strict_slashes=False)
@required_token
def number_profiles(sync):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': User.count()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 400



if __name__ == '__main__':
    profile.run()

# flask --app app run --debug
