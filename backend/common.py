#!/usr/bin/env python3
"""
common file
"""
import os
from dotenv import load_dotenv

load_dotenv()

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.environ.get('FLASK_UPLOAD_FOLDER'))
ALLOWED_EXTENSIONS = os.environ.get('FLASK_ALLOWED_EXTENSIONS').split(',')
MAX_CONTENT_LENGTH = int(os.environ.get('FLASK_MAX_CONTENT_LENGTH'))