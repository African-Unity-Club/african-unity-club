#!/usr/bin/env python3
"""MongoDB database"""
from pymongo import MongoClient
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


class MongoConfig:
    """MongoDB configuration"""

    def __init__(self, uri: str, dbname: str):
        """Initialize MongoDB configuration"""

        self.__client = MongoClient(uri)
        self.__database = self.__client[dbname]
    

    @property
    def database(self) -> pymongo.database.Database:
        """Return MongoDB client"""
        return self.__database


MongoConfig = MongoConfig(
    f"mongodb://{os.environ.get('MONGO_HOST')}:{os.environ.get('MONGO_PORT')}",
    os.environ.get('MONGO_DBNAME')
)
