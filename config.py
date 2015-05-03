# -*- coding: utf-8 -*-

class Config:
	DEBUG = False
	TESTING = False

class DevelopmentConfig(Config):
	DEBUG = True
	TESTING = True
	MONGODB_SETTINGS = {
		'db': 'docer',
		'host': '127.0.0.1',
		'port': 27017
	}