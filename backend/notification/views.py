#!/usr/bin/env python3
"""notification views"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Notifications, Reads

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

notif = Flask(__name__)

notif.config['ENV'] = os.environ.get('FLASK_ENV')
notif.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
notif.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
notif.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(notif, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@notif.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@notif.errorhandler(401)
def unauthorized(error):
    """ unnotiforized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@notif.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@notif.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@notif.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



# envoyer une notification
@notif.route('/send-notifications', methods=['POST'], strict_slashes=False)
@required_token
def send_notifications(sync):
    """ send notifications """
    data = request.get_json()
    if not data:
        abort(400, 'Invalid data')

    try:
        return jsonify(
            {
                'message': 'success',
                'data': Notifications.create(data)
            }
        ), 201
    except Exception as error:
        return jsonify(
            {
                'message': 'error',
                'data': str(error)
            }
        ), 500


# lire une notification
@notif.route('/read-notifications/<string:notif>', methods=['POST'], strict_slashes=False)
@required_token
def read_notifications(sync, notif: str):
    """ read notifications """
    data = request.get_json()
    if not data:
        abort(400, 'Invalid data')

    try:
        return jsonify(
            {
                'message': 'success',
                'data': Reads.create(data)
            }
        ), 201
    except Exception as error:
        return jsonify(
            {
                'message': 'error',
                'data': str(error)
            }
        ), 500


# lire toutes les notifications
@notif.route('/read-all-notifications', methods=['POST'], strict_slashes=False)
@required_token
def read_all_notifications(sync):
    """ read all notifications """
    data = request.get_json()
    if not data:
        abort(400, 'Invalid data')

    try:
        return jsonify(
            {
                'message': 'success',
                'data': Reads.create(data)
            }
        ), 201
    except Exception as error:
        return jsonify(
            {
                'message': 'error',
                'data': str(error)
            }
        ), 500


# supprimer une notification
@notif.route('/delete-notifications/<string:notif>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_notifications(sync, notif: str):
    """ delete notifications """
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Notifications.delete(notif)
            }
        ), 201
    except Exception as error:
        return jsonify(
            {
                'message': 'error',
                'data': str(error)
            }
        ), 500


# supprimer toutes les notifications
@notif.route('/delete-all-notifications', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_all_notifications(sync):
    """ delete all notifications """
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Notifications.delete_all()
            }
        ), 201
    except Exception as error:
        return jsonify(
            {
                'message': 'error',
                'data': str(error)
            }
        ), 500
