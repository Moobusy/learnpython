# -*- coding: utf-8 -*-
'''
	Docer
	~~~~~~
	A document viewing platform.

	:copyright: (c) 2015 by Docer.Org.
	:license: MIT, see LICENSE for more details.
'''

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from app.frontend import frontend as frontend_blueprint
from app.backend import backend as backend_blueprint

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
# mongodb
mongo = MongoEngine(app)
	
def create_app():
	"""Create a flask app with a config."""
	
	app.register_blueprint(frontend_blueprint)
	app.register_blueprint(backend_blueprint, name = 'admin', url_prefix = '/admin')

	return app