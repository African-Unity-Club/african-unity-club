#!/usr/bin/env python3
""" skill views """
from flask import Blueprint, request, jsonify

from .models import Skills

from ..utils.required import required_token


skill = Blueprint('skills', __name__, url_prefix='/skills')



# get all skills of user
@skill.route('/me', methods=['GET'], strict_slashes=False)
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
@skill.route('/me/<id>', methods=['GET'], strict_slashes=False)
@required_token
def get_user_skill(sync, id):

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Skills.get(sync['user_id'], id)
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
@skill.route('/', methods=['POST'], strict_slashes=False)
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
@skill.route('/', methods=['PUT'], strict_slashes=False)
@required_token
def update_skill(sync):
    
    data = request.get_json()
    if not data:
        abort(404)

    try:
        Skills.update(sync['user_id'], data)
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
@skill.route('/', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_skill():

    data = request.get_json()
    if not data:
        abort(400)
    
    try:
        Skills.delete(sync['user_id'], data.get('id'))

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
