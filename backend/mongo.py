#!/usr/bin/env python3
"""MongoDB database"""
from pymongo import MongoClient
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


class MongoConfig:
    """MongoDB configuration"""

    def __init__(self, uri: str):
        """Initialize MongoDB configuration"""
        self.__uri = uri
        self.__client = MongoClient(self.__uri)
    

    @property
    def client(self) -> MongoClient:
        """Return MongoDB client"""
        return self.__client


MongoConfig = MongoConfig(f"mongodb://{os.environ.get('MONGO_HOST')}:{os.environ.get('MONGO_PORT')}")
