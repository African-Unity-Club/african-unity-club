#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt
import base64
import hashlib
from typing import Union


class MPIPwdHash:
    """Encrypting passwords class"""

    def __init__(self):
        """Initialize Encrypt class"""
        self._bcrypt = bcrypt
    
    def b64encode(self, string: Union[str, bytes]) -> bytes:
        """Base64 encode method"""
        assert type(string) is str or type(string) is bytes, 'string must be str or bytes'
        
        return base64.b64encode(
            string.encode('utf-8') if type(string) is str else string
        )
    
    def sha256(self, string: str) -> bytes:
        """SHA256 encode method"""
        assert type(string) is str, 'string must be str'
        
        return hashlib.sha256(
            string.encode('utf-8')
        ).digest()

    def hash_password(self, password: str) -> bytes:
        """Hash password method"""
        assert type(password) is str, 'password must be str'
        
        return self._bcrypt.hashpw(
            self.b64encode(
                self.sha256(password)
            ),
            self._bcrypt.gensalt()
        )

    def is_valid(self, password: str, hashed_password: bytes) -> bool:
        """Validate password method"""
        assert type(password) is str, 'password must be str'
        assert type(hashed_password) is bytes, 'hashed_password must be bytes'
        
        return self._bcrypt.checkpw(
            self.b64encode(
                self.sha256(password)
            ),
            hashed_password
        )

MPIPwdHash = MPIPwdHash()
