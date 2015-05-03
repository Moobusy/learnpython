# -*- coding: utf-8 -*-
'''
	Docer - backtend
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''

from flask import Blueprint

backend = Blueprint('backend', __name__)

# import routes
from . import views