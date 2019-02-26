# -*- coding: utf-8 -*-

# ==================================== Meta ==================================== #
'''
Author: Ankit Murdia
Version: 0.0.1
Created: 2019-02-15 20:16:23
Updated: 2019-02-17 22:06:44
Description:
Notes:
To do:
'''
# ============================================================================== #


# ================================ Dependencies ================================ #
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_migrate import Migrate
from retstlk import config
# ============================================================================== #


# ================================= Constants ================================== #
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit = False,
										autoflush = False,
										bind = engine))

Base = declarative_base()
Base.query = db_session.query_property()
migrate = None
# ============================================================================== #


# ================================= Code Logic ================================= #
#  Callable methods
def init_db():
	from retstlk.models import schema_orm
	Base.metadata.create_all(bind = engine)

def shutdown_session(exception=None):
	db_session.remove()

def init_app(app):
	global migrate
	migrate = Migrate(app, Base)
	init_db()
	app.teardown_appcontext(shutdown_session)

#  Abstracted classes

# ============================================================================== #


# ================================ CLI Handler ================================= #
if __name__ == "__main__":
	pass
# ============================================================================== #