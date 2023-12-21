#!/usr/bin/env python3
"""
common file
"""
import os
from dotenv import load_dotenv

load_dotenv()

IMAGES_UPLOAD_FOLDER = os.path.normpath(os.environ.get('IMAGES_UPLOAD_FOLDER'))
IMAGES_ALLOWED_EXTENSIONS = os.environ.get('IMAGES_ALLOWED_EXTENSIONS').split(',')
IMAGES_MAX_CONTENT_LENGTH = int(os.environ.get('IMAGES_MAX_CONTENT_LENGTH_STANDARD'))
