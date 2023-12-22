#!/usr/bin/env python3
""" profile API RESTful endpoints """
from flask import Blueprint, request, jsonify


from .models import User

from ..utils.required import required_token
from ..utils.encrypt.mbauth import MobileGoogleAuth
from ..utils.redis import redis_client


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
    try:
        user = User.get(sync['user_id'])
        if user and user['role'] in ('agent', 'controler', 'manager', 'admin', 'superadmin'):
            return jsonify(
                {
                    'message': 'Success',
                    'data': User.all()
                }, 200
            )

        else:
            return jsonify(
                {
                    'message': 'Success',
                    'data': {}
                }, 401
            )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )

# find profiles by query
@profile.route('/search', methods=['GET', 'POST'], strict_slashes=False)
@required_token
def search(sync):

    data = rquest.get_json()
    if not data:
        abort(404)
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': User.find(data)
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }
        )

# get profile by id
@profile.route('/me', methods=['GET'], strict_slashes=False)
@required_token
def me(sync):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': User.get(sync['user_id'])
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': User.get(sync['user_id'])
            }, 401
        )


@profile.route('/user/<string:id>', methods=['GET'], strict_slashes=False)
@required_token
def user(sync, id):
    
    try:
        user = User.get(id)
        act = User.get(sync['user_id'])
        if user and act['role'] in ('agent', 'controler', 'manager', 'admin', 'superadmin'):
            return jsonify(
                {
                    'message': 'Success',
                    'data': user
                }, 200
            )
        else:
            return jsonify(
                {
                    'message': 'Success',
                    'data': {}
                }, 401
            )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )


@profile.route('/user-profile/<string:id>', methods=['GET'], strict_slashes=False)
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
            }, 200
        )
        
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )
    


# update profile by id
@profile.route('/update-me', methods=['PUT'], strict_slashes=False)
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
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )


# update profile password by id
@profile.route('/update-password-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_password_me(sync):
    
    data = request.get_json()
    if not data:
        abort(404)
    
    try:
        if data.get('old_password') != data.get('new_password'):
            return jsonify(
                {
                    'message': 'Error',
                    'data': 'Passwords do not match'
                }, 401
            )
        
        User.update_password(sync['user_id'], data.get('new_password'))

        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )


# update profile avatar by id
def traitement_avatar(avatar, user_id):
    pass

@profile.route('/update-avatar-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_avatar_me(sync):
    
    try:
        if not traitement_avatar(request.get_json().get('avatar'), sync['user_id']):
            return jsonify(
                {
                    'message': 'Error',
                    'data': 'Error'
                }, 401
            )
        User.update_avatar(sync['user_id'], request.get_json().get('avatar'))
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )

# update profile status by id
@profile.route('/update-status-me', methods=['PUT'], strict_slashes=False)
@required_token
def update_status_me(sync):
    pass

# 2FA enable
@profile.route('/2fa-enable', methods=['PUT'], strict_slashes=False)
@required_token
def two_factor_enable(sync):
    
    try:
        _2fa_key = MobileGoogleAuth.keygen

        # enregistrer la clé secrète dans la base de donnée redis
        redis_client.set(sync['user_id'] + '2fa', _2fa_key)

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
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )


# 2FA disable
@profile.route('/2fa-disable', methods=['PUT'], strict_slashes=False)
@required_token
def two_factor_disable(sync):
    
    # supprimer la clé secrète dans la base de donnée redis
    return jsonify(
        {
            'message': 'Success',
            'data': {}
        }, 200
    )


@profile.route('/2fa-verify', methods=['PUT'], strict_slashes=False)
@required_token
def two_factor_verify(sync):
    
    data = request.get_json()
    if not data:
        abort(404)

    try:
        # vérifier le code à usage unique lors de la connexion
        if MobileGoogleAuth.verify(redis_client.get(sync['user_id'] + '2fa'), data.get('code')):
            return jsonify(
                {
                    'message': 'Success',
                    'data': {}
                }, 200
            )
        else:
            return jsonify(
                {
                    'message': 'Error',
                    'data': 'Invalid code'
                }, 401
            )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }, 404
        )

# number of profiles
@profile.route('/number-profiles', methods=['GET'], strict_slashes=False)
@required_token
def number_profiles(sync):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': User.count()
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        )
