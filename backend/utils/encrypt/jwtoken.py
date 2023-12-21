#!/usr/bin/env python3
"""jwt class"""
import jwt
from dotenv import load_dotenv

import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Union



load_dotenv()



class MpiJWT:

    algorithms = 'HS256'
    error = ''

    def __init__(self, SECRET_KEY):

        self.__secretkey = SECRET_KEY
    
    def tokenizer(self, payload: Dict, exp: Optional[int]=None) -> Union[str, bytes]:
        """
        exp (days)
        """

        if exp:
            exp = (datetime.now() + timedelta(days=exp)).timestamp()
        
        payload['exp'] = exp or (datetime.now() + timedelta(days=30)).timestamp()
        return jwt.encode(payload, self.__secretkey, algorithm=self.algorithms)
    
    def analyze(self, token: Union[str, bytes]):

        try:
            payload = jwt.decode(token, self.__secretkey, algorithms=[self.algorithms])
            return payload
        
        except jwt.ExpiredSignatureError:
            self.error = 'expired token'
            return None
        
        except jwt.InvalidTokenError:
            self.error = 'invalid token'
            return None
    
    def expired(self):
        self.expired = datetime.utcnow() - timedelta(minutes=5)


MpiJWT = MpiJWT(os.environ.get('JWT_SECRET_KEY'))