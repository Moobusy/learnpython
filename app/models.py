# -*- coding: utf-8 -*-
'''
	Docer - models
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''
from datetime import datetime
from . import mongo

class Users(mongo.Document):
	"""The users document of Docer"""

	username = mongo.StringField(min_length = 5, max_length = 50, unique = True, required = True)
	password = mongo.StringField(min_length = 8, max_length = 50, required = True)
	created_at = mongo.DateTimeField(default = datetime.now(), required = True)

	meta = {
		# 索引
		'indexes': ['username'],
		# 默认排序
		'ordering': ['-created_at']
	}
	