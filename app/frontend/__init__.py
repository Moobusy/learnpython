# -*- coding: utf-8 -*-
'''
	backend
'''

from flask import Blueprint

frontend = Blueprint('frontend', __name__)

# import routes
from . import views