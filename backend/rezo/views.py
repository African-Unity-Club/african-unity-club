#!/usr/bin/env
""" rezeriences views """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Reseaux

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

rez = Flask(__name__)

rez.config['ENV'] = os.environ.get('FLASK_ENV')
rez.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
rez.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
rez.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(rez, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@rez.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@rez.errorhandler(401)
def unauthorized(error):
    """ unrezorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@rez.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@rez.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@rez.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



# user reseaux
@rez.route('/me-socials', methods=['GET'], strict_slashes=False)
@required_token
def rez(sync):
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Reseaux.find({'user_id': sync['user_id']})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


# user reseau
@rez.route('/me-social/<id>', methods=['GET'], strict_slashes=False)
@required_token
def rez(sync, id):
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Reseaux.get(id, sync['user_id'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500
    

# user reseau create
@rez.route('/me-social-create', methods=['POST'], strict_slashes=False)
@required_token
def rez(sync):
    try:
        data = request.get_json()
        data['user_id'] = sync['user_id']
        return jsonify(
            {
                'message': 'success',
                'data': Reseaux.create(data)
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


# user reseau update
@rez.route('/me-social-update/<id>', methods=['PUT'], strict_slashes=False)
@required_token
def rez(sync):

    data = request.get_json()
    if not data:
        abort(400, 'Invalid data')
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Reseaux.update(id, sync['user_id'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


# user reseau delete
@rez.route('/me-social-delete/<id>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_rez(sync, id):
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Reseaux.delete(id, sync['user_id'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


if __name__ == '__main__':
    rez.run()
