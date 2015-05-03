# -*- coding: utf-8 -*-
'''
	front
'''

from . import frontend

@frontend.route('/')
def hello_world():
	return "Hello World!2"
