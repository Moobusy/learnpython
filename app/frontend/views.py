# -*- coding: utf-8 -*-
'''
	Docer - frontend - views
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''

from . import frontend

@frontend.route('/')
def hello_world():
	return "Hello World!"