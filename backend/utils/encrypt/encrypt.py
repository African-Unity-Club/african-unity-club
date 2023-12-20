#!/usr/bin/env python3
"""Encrypting"""
from .pwdhash import MPIPwdHash



class MPIEncryptor:
    """Encrypting passwords class"""

    def __init__(self):
        """Initialize Encrypt class"""
        pass
    
    @property
    def pwdhash(self):
        """Hash password method"""
        return MPIPwdHash


MPIEncryptor = MPIEncryptor()
