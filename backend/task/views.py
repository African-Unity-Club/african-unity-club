#!/usr/bin/env python3
"""task views"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Tasks, LiveSession, TimeStamp

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

tsk = Flask(__name__)

tsk.config['ENV'] = os.environ.get('FLASK_ENV')
tsk.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
tsk.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
tsk.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(tsk, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@tsk.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@tsk.errorhandler(401)
def unauthorized(error):
    """ untskorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@tsk.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@tsk.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@tsk.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500


# planifier une tache
@tsk.route('/create-task', methods=['POST'], strict_slashes=False)
@required_token
def create_task(sync):
    """ create task """
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    try:
        return jsonify(
            {
                'message': 'Task created',
                'data': Tasks.create(data)
            }
        ), 201
    except KeyError as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


# lister toutes les tache d'un user
@tsk.route('/tasks', methods=['GET'], strict_slashes=False)
@required_token
def user_tasks(sync):
    """ user tasks """
    try:
        return jsonify(
            {
                'message': 'Tasks list',
                'data': Tasks.find({'user_id': sync['user_id']})
            }
        ), 200
    except KeyError as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


# un tache d'un user
@tsk.route('/task/<string:id>', methods=['GET'], strict_slashes=False)
@required_token
def user_task(sync, id):
    """ user task """
    try:
        return jsonify(
            {
                'message': 'Task',
                'data': Tasks.get(id)
            }
        ), 200
    except KeyError as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


# modifier une tache d'un user
@tsk.route('/update-task/<string:id>', methods=['PUT'], strict_slashes=False)
@required_token
def update_task(sync, id):
    """ update task """
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    try:
        return jsonify(
            {
                'message': 'Task updated',
                'data': Tasks.update(id, data, sync['user_id'])
            }
        ), 200
    except KeyError as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


# supprimer une tache d'un user
@tsk.route('/delete-task/<string:id>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_task(sync, id):
    """ delete task """
    try:
        return jsonify(
            {
                'message': 'Task deleted',
                'data': Tasks.delete(id, sync['user_id'])
            }
        ), 200
    except KeyError as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


# ajouter des inviter a une tache
@tsk.route('/add-friend/<string:id>', methods=['PUT'], strict_slashes=False)
@required_token
def add_friend(sync, id):
    """ add friend """
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    try:
        return jsonify(
            {
                'message': 'Friend added',
                'data': Tasks.ask(id, data, sync['user_id'])
            }
        ), 200
    except KeyError as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


# ajouter un timestamp en planning d'un task
@tsk.route('/add-timestamp/<string:id>', methods=['PUT'], strict_slashes=False)
@required_token
def add_timestamp(sync, id):
    """ add timestamp """
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    try:
        return jsonify(
            {
                'message': 'Timestamp added',
                'data': TimeStamp.create(data)
            }
        ), 200
    except KeyError as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


# modifier un timestamp


# supprimer un timestamp


# lancer un live session


# arreter un live session