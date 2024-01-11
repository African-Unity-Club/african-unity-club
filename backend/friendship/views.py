#!/usr/bin/env python3
"""friendship views"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Friends, Followers, Followings

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

frd = Flask(__name__)

frd.config['ENV'] = os.environ.get('FLASK_ENV')
frd.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
frd.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
frd.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(frd, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@frd.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@frd.errorhandler(401)
def unauthorized(error):
    """ unfrdorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@frd.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@frd.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@frd.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500


# friend request
@frd.route('/friend-request/<friend>', methods=['POST'], strict_slashes=False)
@required_token
def friend_request(user_id: str, friend) -> Dict:
    """ friend request """
    try:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid JSON")
        
        data['friend_id'] = friend
        return jsonify(
            {
                'message': 'friend request created',
                'data': Friends.create(data)
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'friend request not created',
                'data': str(e)
            }
        ), 400

# action to friend
@frd.route('/friend-action/<id>', methods=['PUT'], strict_slashes=False)
@required_token
def friend_action(user_id: str, id) -> Dict:
    """ friend action """
    try:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid JSON")
        
        return jsonify(
            {
                'message': 'friend action updated',
                'data': Friends.update(id, data, user_id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'friend action not updated',
                'data': str(e)
            }
        ), 400


# all friends
@frd.route('/friends', methods=['GET'], strict_slashes=False)
@required_token
def all_friends(user_id: str) -> Dict:
    """ all friends """
    try:
        return jsonify(
            {
                'message': 'all friends',
                'data': Friends.all(user_id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'friends not found',
                'data': str(e)
            }
        ), 404

# follow
@frd.route('/follow/<friend>', methods=['POST'], strict_slashes=False)
@required_token
def follow(user_id: str, friend) -> Dict:
    """ follow """
    try:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid JSON")
        
        data['friend_id'] = friend
        return jsonify(
            {
                'message': 'follow created',
                'data': Followers.create(data)
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'follow not created',
                'data': str(e)
            }
        ), 400


# unfollow
@frd.route('/unfollow/<id>', methods=['DELETE'], strict_slashes=False)
@required_token
def unfollow(user_id: str, id) -> Dict:
    """ unfollow """
    try:
        return jsonify(
            {
                'message': 'follow deleted',
                'data': Followers.delete(id, user_id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'follow not deleted',
                'data': str(e)
            }
        ), 400

# all followers
@frd.route('/followers', methods=['GET'], strict_slashes=False)
@required_token
def all_followers(user_id: str) -> Dict:
    """ all followers """
    try:
        return jsonify(
            {
                'message': 'all followers',
                'data': Followers.all(user_id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'followers not found',
                'data': str(e)
            }
        ), 404

# all followings
@frd.route('/followings', methods=['GET'], strict_slashes=False)
@required_token
def all_followings(user_id: str) -> Dict:
    """ all followings """
    try:
        return jsonify(
            {
                'message': 'all followings',
                'data': Followings.all(user_id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'followings not found',
                'data': str(e)
            }
        ), 404