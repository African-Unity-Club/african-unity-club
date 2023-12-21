#!/usr/bin/env python3
"""Encrypting"""
from .pwdhash import MPIPwdHash
from .jwtoken import MpiJWT
from .mbauth import MobileGoogleAuth



class MPIEncryptor:
    """Encrypting passwords class"""

    def __init__(self):
        """Initialize Encrypt class"""
        pass
    
    @property
    def pwdhash(self):
        """Hash password method"""
        return MPIPwdHash
    
    @property
    def jwt(self):
        """JWT method"""
        return MpiJWT
    
    @property
    def auth2fa(self):
        """2FA method"""
        return MobileGoogleAuth


MPIEncryptor = MPIEncryptor()
