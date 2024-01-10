#!/usr/bin/env
""" like, share, repost and comment views """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Actions

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

lsr = Flask(__name__)

lsr.config['ENV'] = os.environ.get('FLASK_ENV')
lsr.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
lsr.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
lsr.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(lsr, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@lsr.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@lsr.errorhandler(401)
def unauthorized(error):
    """ unlsrorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@lsr.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@lsr.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@lsr.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500


@lsr.route('/lsr/<action>', methods=['GET'], strict_slashes=False)
@required_token
def actions(sync, action):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Actions.find({'user_id': sync['user_id'], 'action': action})
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 500


@lsr.route('/lsr/<action>/<id>', methods=['GET'], strict_slashes=False)
@required_token
def action(sync, action, id):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Actions.find({'user_id': sync['user_id'], 'action': action, 'post_id': id})
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 500


@lsr.route('/lsr/<action>/create', methods=['POST'], strict_slashes=False)
@required_token
def create_lsr(sync, action):
    data: Dict = request.get_json()
    if not data:
        abort(404)

    data['user_id'] = sync['user_id']
    data['action'] = action

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Actions.create(data)
            }
        ), 201

    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 500


@lsr.route('/lsr/<action>/<id>/update', methods=['PUT'], strict_slashes=False)
@required_token
def update_lsr(sync, action, id):
    data: Dict = request.get_json()
    if not data:
        abort(404)

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Actions.update(id, data, sync['user_id'])
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 500


@lsr.route('/lsr/<action>/<id>/delete', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_lsr(sync, action, id):
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Actions.delete(id, sync['user_id'])
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': str(e)
            }
        ), 500


if __name__ == "__main__":
    lsr.run()
