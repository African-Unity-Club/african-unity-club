#!/usr/bin/env python3
"""chat views"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Chats, MAction

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

sms = Flask(__name__)

sms.config['ENV'] = os.environ.get('FLASK_ENV')
sms.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
sms.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
sms.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(sms, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@sms.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@sms.errorhandler(401)
def unauthorized(error):
    """ unsmsorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@sms.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@sms.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@sms.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



@sms.route('/chat-direct/<receiver>', methods=['POST'], strict_slashes=False)
@required_token
def direct(sync, receiver):
    
    # les messages ou je suis le sender
    # les messages ou je suis le receiver
    # mis a jour de tous les messages ou je suis le receiver avec read a True
    # fais l'addition des deux listes et les tries par date
    # renvois la liste
    pass


@sms.route('/chat-group/<group>', methods=['POST'], strict_slashes=False)
@required_token
def group(sync, group):
    
    # tous les messages du groupe ou channel trier par date
    # mis a jour de tous les messages du groupe avec read a True
    # renvois la liste
    pass
        
        

@sms.route('/archived/<archlist>', methods=['POST'], strict_slashes=False)
@required_token
def archived(sync, archlist):
    # prendre la liste des messages a archiver (archlist(ids))
    # mis a jour de tous les messages de la liste avec archived a True
    pass


@sms.route('/trash/<trashlist>', methods=['POST'], strict_slashes=False)
@required_token
def trash(sync, trashlist):
    # prendre la liste des messages a trash (trashlist(ids))
    # mis a jour de tous les messages de la liste avec trash a True
    pass


@sms.route('/trash-all/<trashlist>', methods=['POST'], strict_slashes=False)
@required_token
def trash_all(sync, trashlist):
    # prendre la liste des messages a trash (trashlist(ids))
    # mis a jour de tous les messages de la liste avec trash a True
    pass


@sms.route('/favorite/<favorlist>', methods=['POST'], strict_slashes=False)
@required_token
def favorite(sync, favorlist):
    # prendre la liste des messages a favorite (favorlist(ids))
    # mis a jour de tous les messages de la liste avec favorite a True
    pass


@sms.route('/epingle/<id>', methods=['POST'], strict_slashes=False)
@required_token
def epingle(sync, id):
    # prendre la liste des messages a epingle (id)
    # mis a jour de tous les messages de la liste avec epingle a True
    pass

