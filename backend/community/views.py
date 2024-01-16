#!/usr/bin/env python3
"""community views"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Community

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

cmty = Flask(__name__)

cmty.config['ENV'] = os.environ.get('FLASK_ENV')
cmty.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
cmty.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
cmty.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(cmty, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@cmty.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@cmty.errorhandler(401)
def unauthorized(error):
    """ uncmtyorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@cmty.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@cmty.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@cmty.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



@cmty.route('/communities', methods=['GET'], strict_slashes=False)
@required_token
def communities(sync):
    """get all communities"""

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.all()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@cmty.route('/community/<domain>', methods=['GET'], strict_slashes=False)
@required_token
def communities_domain(sync, domain):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.find({'domain': domain})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }
        ), 400


@cmty.route('/community/<owner>', methods=['GET'], strict_slashes=False)
@required_token
def communities_owner(sync, owner):
    
    try:
        return jsonify(
            {
                'message': "Success",
                "data": Community.find({'owner': owner})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                "data": str(e)
            }
        ), 400


@cmty.route('/community/<member>', methods=['GET'], strict_slashes=False)
@required_token
def member_communities(sync, member):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.find({'members': member})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }
        ), 400


@cmty.route('/community/<admin>', methods=['GET'], strict_slashes=False)
@required_token
def admin_communities(sync, admin):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.find({'admins': admin})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }
        ), 400


@cmty.route('/community/<moderator>', methods=['GET'], strict_slashes=False)
@required_token
def moderator_communities(sync, moderator):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.find({'moderators': moderator})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }
        ), 400


@cmty.route('/community/<manager>', methods=['GET'], strict_slashes=False)
@required_token
def manager_communities(sync, manager):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.find({'managers': manager})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'Success',
                'data': str(e)
            }
        ), 400


@cmty.route('/community/<id>', methods=['GET'], strict_slashes=False)
@required_token
def community(sync, id):
    """get one community"""

    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.get(id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@cmty.route('/creta-community', methods=['POST'], strict_slashes=False)
@required_token
def create_community(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    data['owner'] = sync['user_id']
    
    try:
        return jsonify(
            {
                'message': 'Succes',
                "data": Community.create(data)
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                "data": str(e)
            }
        ), 500


@cmty.route('/update-community/<id>', methods=['PUT'], strict_slashes=False)
@required_token
def update_comminity(sync, id):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.update(id, data, sync['user_id'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@cmty.route('/comminuty-ownership', methods=['PUT'], strict_slashes=False)
@required_token
def ownership_community(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.ownership(data['id'], data['owner'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@cmty.route('/add-memeber', methods=['GET'], strict_slashes=False)
@required_token
def add_member(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.add_member(data['id'], data['member'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@cmty.route('/remove-member', methods=['GET'], strict_slashes=False)
@required_token
def remove_member(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.remove_member(data['id'], data['member'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@cmty.route('/add-admin', methods=['GET'], strict_slashes=False)
@required_token
def add_admin(sync):
        
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.add_admin(data['id'], data['admin'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@cmty.route('/remove-admin', methods=['GET'], strict_slashes=False)
@required_token
def remove_admin(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.remove_admin(data['id'], data['admin'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        )


@cmty.route('/add-moderator', methods=['GET'], strict_slashes=False)
@required_token
def add_moderator(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                "message": "Success",
                "data": Community.add_moderator(data['id'], data['moderator'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "message": "error",
                "data": str(e)
            }
        ), 500


@cmty.route('/remove-moderator', methods=['GET'], strict_slashes=False)
@required_token
def remove_moderator(sync):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.remove_moderator(data['id'], data['moderator'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        )


@cmty.route('/add-manager', methods=['GET'], strict_slashes=False)
@required_token
def add_manager(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                "message": "Success",
                "data": Community.add_manager(data['id'], data['manager'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "message": "error",
                "data": str(e)
            }
        ), 500


@cmty.route('/remove-manager', methods=['GET'], strict_slashes=False)
@required_token
def remove_manager(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
            {
                "message": "Success",
                "data": Community.remove_manager(data['id'], data['manager'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "message": "error",
                "data": str(e)
            }
        ), 500


@cmty.route('/update-avatar', methods=['PUT'], strict_slashes=False)
@required_token
def update_avatar(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.update_avatar(data['id'], data['avatar'], sync['user_id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500


@cmty.route('/update-cover', methods=['PUT'], strict_slashes=False)
@required_token
def update_cover(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.update_cover(data['id'], data['cover'], sync['user_id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500


@cmty.route('/update-visibility', methods=['PUT'], strict_slashes=False)
@required_token
def update_visibility(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.update_visibility(data['id'], data['visibility'], sync['user_id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500


@cmty.route('/create-group', methods=['PUT'], strict_slashes=False)
@required_token
def create_group(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        Community.create_group(data['id'], data['group'], sync['user_id'])
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.get(data['id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500


@cmty.route('/add-group', methods=['PUT'], strict_slashes=False)
@required_token
def add_group(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        Community.add_group(data['id'], data['group'], sync['user_id'])
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.get(data['id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500


@cmty.route('/remove-group', methods=['PUT'], strict_slashes=False)
@required_token
def remove_group(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        Community.remove_group(data['id'], data['group'], sync['user_id'])
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.get(data['id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500


@cmty.route('/remove-cover', methods=['PUT'], strict_slashes=False)
@required_token
def remove_cover(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        Community.remove_cover(data['id'], sync['user_id'])
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.get(data['id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500


@cmty.route('/remove-avatar', methods=['PUT'], strict_slashes=False)
@required_token
def remove_avatar(sync):
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    try:
        Community.remove_avatar(data['id'], sync['user_id'])
        return jsonify(
                {
                    'message': 'Success',
                    'data': Community.get(data['id'])
                }
            ), 200
    except Exception as e:
        return jsonify(
                {
                    'message': 'error',
                    'data': str(e)
                }
            ), 500

@cmty.route('/delete-community/<id>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_community(sync, id):
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data': Community.delete(id, sync['user_id'])
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
    cmty.run()
