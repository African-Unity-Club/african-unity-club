#!/usr/bin/env python3
""" skill views """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Skills

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

skill = Flask(__name__)

skill.config['ENV'] = os.environ.get('FLASK_ENV')
skill.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
skill.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
skill.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(skill, resources={r"/*": {"origins": "*"}})



# gestion d'erreur
@skill.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@skill.errorhandler(401)
def unauthorized(error):
    """ unskillorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@skill.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@skill.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@skill.errorhandler(Exception)
def internal_server_error(error):
    """ internal server error """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



# get all skills of user
@skill.route('/me-skills', methods=['GET'], strict_slashes=False)
@required_token
def get_user_skills(sync):

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Skills.find({'user_id': sync['user_id']})
            }, 200
        )
    
    except Exception as e:

        return jsonify(
            {
                'message': 'Error',
                'data': {}
            }, 400
        )


# get skill of user
@skill.route('/me-skill/<id>', methods=['GET'], strict_slashes=False)
@required_token
def get_user_skill(sync, id):

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Skills.get(id, user_id=sync['user_id'])
            }, 200
        )
    
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': {}
            }, 400
        )


# create skill of user
@skill.route('/me-create-skill', methods=['POST'], strict_slashes=False)
@required_token
def create_skill(sync):

    data = request.get_json()
    if not data:
        abort(404)
    
    try:
        data['user_id'] = sync['user_id']
        return jsonify(
            {
                'message': 'Success',
                'data': Skills.create(data)
            }, 201
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': {}
            }, 400
        )


# update skill of user
@skill.route('/me-update-skill/<id>', methods=['PUT'], strict_slashes=False)
@required_token
def update_skill(sync, id):
    
    data = request.get_json()
    if not data:
        abort(404)

    try:
        Skills.update(id=id, data=data, user=sync['user_id'])
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
                'data': {}
            }, 400
        )


# delete skill of user
@skill.route('/me-delete-skill/<id>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_skill(sync, id):

    try:
        Skills.delete(id=id, user=sync['user_id'])

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
                'data': {}
            }, 400
        )



if __name__ == '__main__':
    skill.run()

# flask --app app run --debug
