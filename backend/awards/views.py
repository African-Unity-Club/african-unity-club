#!/usr/bin/env
""" award views """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv
import requests

from .models import Awards

from ..utils.required import required_token

from typing import Dict
import os
import json


load_dotenv()

award = Flask(__name__)

award.config['ENV'] = os.environ.get('FLASK_ENV')
award.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
award.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
award.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(award, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@award.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@award.errorhandler(401)
def unauthorized(error):
    """ unawardorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@award.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@award.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@award.errorhandler(Exception)
def internal_server_error(error):
    """ internal server error """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



# all awards of user
@award.route('/me-awards', methods=['GET'], stricte_slashes=False)
@required_token
def me_awards(sync):

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Awards.find({'user_id': sync['user_id']})
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': {}
            }, 400
        )


# award of user
@award.route('/me-award/<id>', methods=['GET'], stricte_slashes=False)
@required_token
def award(sync, id):

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Awards.get(id, user_id=sync['user_id'])
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': {}
            }, 400
        )


# create award of user
@award.route('/me-create-award', methods=['POST'], stricte_slashes=False)
@required_token
def create_award(sync):

    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    
    data['user_id'] = sync['user_id']

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Awards.create(data)
            }, 200
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'Error',
                'data': {}
            }, 400
        )


# update award of user
@award.route('/update-award/<id>', methods=[''], stricte_slashes=False)
@required_token
def update_award(sync, id):

    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')

    try:
        Awards.update(user=sync['user_id'], id=id, data=data)
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


# delete award of user
@award.route('/delete-award/<id>', methods=[''], stricte_slashes=False)
@required_token
def delete_award(sync, id):

    try:
        Awards.delete(id, user_id=sync['user_id'])
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
    award.run()

