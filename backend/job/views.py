#!/usr/bin/env python3
"""job alert views"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

from .models import Jobs, Alerts

from ..utils.required import required_token

from typing import Dict
import os


load_dotenv()

job = Flask(__name__)

job.config['ENV'] = os.environ.get('FLASK_ENV')
job.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT')
job.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST')
job.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
cors = CORS(job, resources={r"/*": {"origins": "*"}})



# gestion d'erreur
@job.errorhandler(400)
def bad_request(error):
    """ bad request """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 400


@job.errorhandler(401)
def unauthorized(error):
    """ unjoborized """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 401


@job.errorhandler(403)
def forbidden(error):
    """ forbidden """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 403


@job.errorhandler(404)
def not_found(error):
    """ not found """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 404


@job.errorhandler(Exception)
def exception_handler(error):
    """ exception """
    return jsonify(
        {
            'message': str(error),
            'data': {}
        }
    ), 500



@job.route('/jobs', methods=['GET'], strict_slashes=False)
@required_token
def jobs(sync):
    """get all jobs"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.all()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/alerts', methods=['GET'], strict_slashes=False)
@required_token
def alerts(sync):
    """get all alerts"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Alerts.find({'user_id': sync['user_id']})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/jobs/<title>', methods=['GET'], strict_slashes=False)
@required_token
def job_by_title(sync, title):
    """get job by title"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.find({'title': title})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/jobs/<domain>', methods=['GET'], strict_slashes=False)
@required_token
def job_by_domain(sync, domain):
    """get job by domain"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.find({'domain': domain})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/jobs/<country>', methods=['GET'], strict_slashes=False)
@required_token
def job_by_country(sync, country):
    """get job by country"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.find({'country': country})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/jobs/<contract>', methods=['GET'], strict_slashes=False)
@required_token
def job_by_contract(sync, contract):
    """get job by contract"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.find({'contract': contract})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/job/<jtype>', methods=['GET'], strict_slashes=False)
@required_token
def job_by_type(sync, jtype):
    """get job by type"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.find({'type': jtype})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/job/<salary>', methods=['GET'], strict_slashes=False)
@required_token
def job_by_salary(sync, salary):
    """get job by salary"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.find({'salary': salary})
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/job/<id>', methods=['GET'], strict_slashes=False)
@required_token
def job_by_id(sync, id):
    """get job by id"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.get(id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/alert/<id>', methods=['GET'], strict_slashes=False)
@required_token
def alert_by_id(sync, id):
    """get alert by id"""
    
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Alerts.get(id)
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 500


@job.route('/create-job', methods=['POST'], strict_slashes=False)
@required_token
def create_job(sync):
    """create job"""
    data: Dict = request.get_json()
    if not data:
        abort(404)

    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.create(data)
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


@job.route('/create-alert', methods=['POST'], strict_slashes=False)
@required_token
def create_alert(sync):
    """create alert"""
    data: Dict = request.get_json()
    if not data:
        abort(404)

    data['user_id'] = sync['user_id']

    try:
        return jsonify(
            {
                'message': 'success',
                'data': Alerts.create(data)
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


@job.route('/update-job/<id>', methods=['PUT'], strict_slashes=False)
@required_token
def update_job(sync, id):
    """update job"""
    data: Dict = request.get_json()
    if not data:
        abort(404)

    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.update(id, data, sync['user_id'])
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


@job.route('/update-alert/<id>', methods=['PUT'], strict_slashes=False)
@required_token
def update_alert(sync, id):
    """update alert"""
    data: Dict = request.get_json()
    if not data:
        abort(404)

    try:
        return jsonify(
            {
                'message': 'success',
                'data': Alerts.update(id, data, sync['user_id'])
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


@job.route('/delete-job/<id>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_job(sync, id):
    """delete job"""
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Jobs.delete(id, sync['user_id'])
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400


@job.route('/delete-alert/<id>', methods=['DELETE'], strict_slashes=False)
@required_token
def delete_alert(sync, id):
    """delete alert"""
    try:
        return jsonify(
            {
                'message': 'success',
                'data': Alerts.delete(id, sync['user_id'])
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'message': 'error',
                'data': str(e)
            }
        ), 400
