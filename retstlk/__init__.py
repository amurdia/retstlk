# -*- coding: utf-8 -*-

# ==================================== Meta ==================================== #
'''
Author: Ankit Murdia
Version: 0.0.1
Created: 2019-02-16 19:06:12
Updated: 2019-02-17 22:04:06
Description:
Notes:
To do:
'''
# ============================================================================== #


# ================================ Dependencies ================================ #
import os
from flask import Flask
from retstlk.helpers import orm_helper
# ============================================================================== #


# ================================= Constants ================================== #

# ============================================================================== #


# ================================= Code Logic ================================= #
#  Callable methods
def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE = os.path.join(app.instance_path, 'retstlk.sqlite')
	)

	if not test_config:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except Exception as e:
		pass

	@app.route('/hello')
	def hello():
		return "Hello World!"

	orm_helper.init_app(app)

	return app
#  Abstracted classes

# ============================================================================== #


# ================================ CLI Handler ================================= #
if __name__ == "__main__":
	pass
# ============================================================================== #