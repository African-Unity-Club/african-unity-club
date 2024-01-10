#!/usr/bin/env python3
""" posts views """
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Posts

from ..utils.required import required_token

import os


load_dotenv()

post = Flask(__name__)

post.config['ENV'] = os.environ.get('FLASK_ENV')
post.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
post.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
post.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(post, resources={r"/*": {"origins": "*"}})


# gestion d'erreur
@post.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@post.errorhandler(401)
def unauthorized(error):
    """ unpostorized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@post.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@post.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@post.errorhandler(Exception)
def internal_server_error(error):
    """ internal server error """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500


@post.route('/posts/<string:reference>', methods=['GET'], strict_slashes=False)
@required_token
def posts_by_reference(sync, reference):
    """ posts by reference """
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.find({'reference': reference})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@post.route('/posts/<reference>/<author>', methods=['GET'], strict_slashes=False)
@required_token
def posts_by_reference_and_author(sync, reference, author):
    """_summary_

    Args:
        sync (_type_): _description_
        reference (_type_): _description_
        author (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    try:
        return jsonify(
            {
                'message': 'Success',
                'data':Posts.find({'reference': reference, 'author': author})
            }
        )
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        )


@post.route('/posts/<string:id>', methods=['GET'], strict_slashes=False)
@required_token
def post_by_id(sync, id):
    """ post by id """
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.get(id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@post.route('/create-post', methods=['POST'], strict_slashes=False)
@required_token
def create_post(sync):
    """ create post """
    
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    
    data['author'] = sync['user_id']
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.create(data)
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@post.route('/update-post/<string:id>', methods=['PUT'], strict_slashes=False)
@required_token
def update_post(sync, id):
    """ update post """
    
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.update(id, data)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@post.route('/publish-post/<string:id>', methods=['PUT'], strict_slashes=False)
@required_token
def publish_post(sync, id):
    """ publish post """
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.publish(id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@post.route('/delete-post/<string:id>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_post(sync, id):
    """ delete post """
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.delete(id, sync['user_id'])
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@post.route('/add-tag/<id>', methods=['POST'], strict_slashes=False)
@required_token
def add_tag(sync, id):
    """ add tag """
    
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    
    tag = data.get('tag')
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.add_tag(id, tag)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@post.route('/remove-tag/<id>', methods=['POST'], strict_slashes=False)
@required_token
def remove_tag(sync, id):
    """ remove tag """
    
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON')
    
    tag = data.get('tag')
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Posts.remove_tag(id, tag)
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
    post.run()
