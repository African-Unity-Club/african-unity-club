#!/usr/bin/env python3
""" profile API RESTful endpoints """
from flask import Blueprint, request, jsonify

from profile.models import User


profile = Blueprint('profile', __name__, url_prefix='/profile')


# get all profiles
@profile.route('/', methods=[], strict_slashes=False)

# find profiles by query
@profile.route('/', methods=[], strict_slashes=False)

# get profile by id
@profile.route('/', methods=[], strict_slashes=False)

# update profile by id
@profile.route('/', methods=[], strict_slashes=False)

# update profile password by id
@profile.route('/', methods=[], strict_slashes=False)

# update profile avatar by id
@profile.route('/', methods=[], strict_slashes=False)

# update profile status by id
@profile.route('/', methods=[], strict_slashes=False)

# number of profiles
@profile.route('/', methods=[], strict_slashes=False)
