#!/usr/bin/env python3
""" token required file """
from flask import request, abort
from utils.encrypt.encrypt import MPIEncryptor as Encrypt

from functools import wraps

from users.models import User



# jwt token
def required_token(f):
    """token_required decorator."""
    @wraps(f)
    def decorated(*args, **kwargs):
        """decorated."""
        
        auth = request.headers.get('Authorization')
        if not auth:
            abort(401, 'token is missing')
        
        if not auth.startswith('--AUC-- '):
            abort(401, 'invalid token')
        
        token = auth.split('--AUC-- ')[1]

        payload = Encrypt.jwt.analyze(token)
        if not payload:
            abort(401, Encrypt.jwt.error)
            
        if User.get(payload['user_id'])['status'] == 'inactive':
            abort(401, 'user is inactive')

        return f(*args, user_id=payload['user_id'], **kwargs)

    return decorated

