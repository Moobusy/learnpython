# -*- coding: utf-8 -*-
'''
	Docer - backend - views
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''

from . import backend

@backend.route('/')
def hello_world():
	return "Hello admin!"