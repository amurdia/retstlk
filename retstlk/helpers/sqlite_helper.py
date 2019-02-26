# -*- coding: utf-8 -*-

# ==================================== Meta ==================================== #
'''
Author: Ankit Murdia
Version: 0.0.1
Created: 2019-01-25 08:48:19
Updated: 2019-01-25 10:27:21
Description:
Notes:
To do:
'''
# ============================================================================== #


# ================================ Dependencies ================================ #
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
# ============================================================================== #


# ================================= Constants ================================== #

# ============================================================================== #


# ================================= Code Logic ================================= #
#  Callable methods
def get_db():
	if 'db' not in g:
		g.db = sqlite3.connect(
			current_app.config['DATABASE'],
			detect_types = sqlite3.PARSE_DECLTYPES
		)
		g.db.row_factory = sqlite3.Row

	return g.db

def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		db.close()

def init_db():
	db = get_db()

	with current_app.open_resource(current_app.config['DATABASE']['schema']) as schema:
		db.executescript(schema.read().decode('utf8'))

	# with open(current_app.config['SCHEMA_PATH']) as schema:
	# 	db.executescript(schema.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
	init_db()
	click.echo("Initialized retstlk database.")

def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)

#  Abstracted classes

# ============================================================================== #


# ================================ CLI Handler ================================= #
if __name__ == "__main__":
	pass
# ============================================================================== #