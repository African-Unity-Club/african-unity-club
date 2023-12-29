#!/usr/bin/env
""" experiences views """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Experiences

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

exp = Flask(__name__)

exp.config['ENV'] = os.environ.get('FLASK_ENV')
exp.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
exp.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
exp.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(exp, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@exp.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@exp.errorhandler(401)
def unauthorized(error):
    """ unexporized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@exp.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@exp.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@exp.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



# user experiences
@exp.route('/me-experiences', methods=['GET'], strict_slashes=False)
@required_token
def me_exps(sync):
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Experiences.find({'user_id': sync['user_id']})
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }, 400
        )


@exp.route('/me-experiences-by-type/<genre>', methods=['GET'], strict_slashes=False)
@required_token
def me_exps_by_type(sync, genre):
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Experiences.find({'user_id': sync['user_id'], 'type': genre})
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }, 400
        )


# user experience
@exp.route('/me-experience/<id>', methods=['GET'], strict_slashes=False)
@required_token
def me_exp(sync, id):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Experiences.get(id, user_id=sync['user_id'])
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }, 400
        )


# user experience create
@exp.route('/me-experience-create', methods=['POST'], strict_slashes=False)
@required_token
def create_exp(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Invalid data')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Experiences.create(data)
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }, 400
        )


# user experience update
@exp.route('/me-experience-update/<id>', methods=['PUT'], strict_slashes=False)
@required_token
def exp(sync, id):
    
    data = request.get_json()
    if not data:
        abort(400, 'Invalid data')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Experiences.update(id, data, sync['user_id'])
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }, 400
        )


# user experience delete
@exp.route('/me-experience-delete/<id>', methods=['DELETE'], strict_slashes=False)
@required_token
def exp(sync, id):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Experiences.delete(id, sync['user_id'])
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }, 400
        )


if __name__ == '__main__':
    exp.run()
