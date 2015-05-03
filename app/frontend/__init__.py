# -*- coding: utf-8 -*-
'''
	Docer - frontend
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''

from flask import Blueprint

frontend = Blueprint('frontend', __name__)

# import routes
from . import views