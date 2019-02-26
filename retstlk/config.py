# -*- coding: utf-8 -*-

# ==================================== Meta ==================================== #
'''
Author: Ankit Murdia
Version: 0.0.1
Created: 2019-01-25 08:18:22
Updated: 2019-01-25 10:16:11
Description:
Notes:
To do:
'''
# ============================================================================== #


# ================================ Dependencies ================================ #
import os.path
# ============================================================================== #


# ================================= Constants ================================== #
CONFIG_TYPE = 'FILE'
SECRET_KEY = '127ef816-6d14-57c4-b238-ab2c3825c74b'
DATA_PATH = '/home/ankit/Code/projects/retstlk/data/'
LOG_PATH = '/home/ankit/Code/projects/retstlk/logs/'
DICT_DB = {
	'mysql': {
		'engine': 'mysql',
		'driver': '',
		'user': 'movoto',
		'pass': 'movoto',
		'host': 'production-48.svcolo.movoto.net',
		'port': '',
		'database': 'retstlk',
		'schema': os.path.abspath('./models/schema_mysql.sql')
	},
	'sqlite': {
		'engine': 'sqlite',
		'driver': '',
		'user': '',
		'pass': '',
		'host': '',
		'port': '',
		'database': os.path.join(DATA_PATH, 'retstlk.sqlite'),
		'schema': os.path.abspath('./models/schema_sqlite.sql')
	}
}
DATABASE = DICT_DB['mysql']
USE_ORM = False
SQLALCHEMY_DATABASE_URI = 'mysql://movoto:movoto@production-48.svcolo.movoto.net:3306/retstlk'
# ============================================================================== #


# ================================= Code Logic ================================= #
#  Callable methods

#  Abstracted classes

# ============================================================================== #


# ================================ CLI Handler ================================= #
if __name__ == "__main__":
	pass
# ============================================================================== #