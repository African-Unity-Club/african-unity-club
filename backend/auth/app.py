#!/usr/bin/env python3
""" authentication file """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

from ..utils.encrypt.encrypt import MPIEncryptor as Encrypt
from ..utils.required import required_token

from ..users.models import User
from ..users.views import create_user

from datetime import datetime, timedelta
import os



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
    
    email = data.get('username')
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
    
    User.update_status(user['_id'], status='active')
    token = Encrypt.jwt.tokenizer({'user_id': user['_id']})
    User.update_last_login(user['_id'], last_login=datetime.now().isoformat())

    user = User.get(user['_id'])
    user['token'] = token
    return jsonify(
        {
            'message': 'Success',
            'data': user
        }, 201
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
    
    token = Encrypt.jwt.tokenizer({'user_id': user[0]['_id']})
    User.update_last_login(user[0]['_id'], last_login=datetime.now().isoformat())
    User.update_status(user[0]['_id'], status='active')
    
    user = User.get(user[0]['_id'])
    user['token'] = token
    
    return jsonify(
        {
            'message': 'Success',
            'data': user
        }
    )


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
    )


if __name__ == '__main__':
    auth.run()

# flask --app app run --debug
