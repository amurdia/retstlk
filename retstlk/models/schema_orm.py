# -*- coding: utf-8 -*-

# ==================================== Meta ==================================== #
'''
Author: Ankit Murdia
Version: 0.0.1
Created: 2019-02-16 06:25:49
Updated: 2019-02-17 22:27:53
Description:
Notes:
To do:
'''
# ============================================================================== #


# ================================ Dependencies ================================ #
from datetime import datetime
from urllib.parse import urlparse, urlunparse
import re
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, backref
from retstlk.helpers.orm_helper import Base
# ============================================================================== #


# ================================= Constants ================================== #
domain_pattern = re.compile(r'www.*?\.')
# ============================================================================== #


# ================================= Code Logic ================================= #
#  Callable methods

#  Abstracted classes
class MLS(Base):
	__tablename__ = 'mls'
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(80), nullable=False)
	user = Column(String(80), nullable=False)
	passw = Column(String(255), nullable=False)
	useragent = Column(String(80))
	useragentpass = Column(String(255))
	rets_url = Column(String(255), nullable=False)
	rets_ver = Column(String(80), nullable=False)
	state = Column(String(80), nullable=False)
	area_covered = Column(String(255), nullable=False)
	association = Column(String(255), nullable=False)
	broker = Column(String(255), nullable=False)
	public_url = Column(String(255))
	created = Column(DateTime, default=datetime.utcnow())
	updated = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

	def __init__(self, title, rets_url, rets_ver, user, passw, state, area_covered, association, broker, useragent='', useragentpass='', public_url=None):
		self.title = title
		self.user = user
		self.passw = passw
		self.useragent = useragent
		self.useragentpass = useragentpass
		self.rets_url = rets_url
		self.rets_ver = rets_ver
		self.state = state
		self.area_covered = area_covered
		self.association = association
		self.broker = broker
		self.public_url = public_url

	def __repr__(self):
		return "<MLS {}>".format(self.title)


class Organization(Base):
	__tablename__ = 'organization'
	id = Column(Integer, primary_key=True, autoincrement=True)
	alias = Column(String(80))
	name = Column(String(80), nullable=False)
	email = Column(String(120), nullable=False)
	phone = Column(String(80), nullable=False)
	address = Column(String(800))
	logo_url = Column(String(255))
	web_url = Column(String(255))
	email_domain = Column(String(80))
	created = Column(DateTime, default=datetime.utcnow())
	updated = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

	def __init__(self, name, email, phone, alias=None, address=None, logo_url=None, web_url=None, email_domain=None):
		self.alias = alias
		self.name = name
		self.email = email
		self.phone = phone
		self.address = address
		self.logo_url = logo_url
		self.web_url = web_url
		self.email_domain = email_domain or (web_url and domain_pattern.sub('', urlparse(web_url).hostname))

	def __repr__(self):
		return "<Organization {}>".format(self.name)

class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key=True, autoincrement=True)
	alias = Column(String(30))
	name = Column(String(80), nullable=False)
	email = Column(String(255), nullable=False)
	phone = Column(String(255))
	org_id = Column(Integer, ForeignKey('organization.id'))
	# organization = relationship('Organization', backref=backref('users', lazy=True), cascade='delete')
	group_id = Column(Integer, ForeignKey('user.id'))
	# group = relationship('User', backref=backref('users', lazy=True), cascade='delete')
	enabled = Column(Boolean, nullable=False, default=1)
	created = Column(DateTime, default=datetime.utcnow())
	updated = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

	def __init__(self, name, email, alias=None, phone=None, org_id=None, group_id=None):
		self.name = name
		self.email = email
		self.alias = alias
		self.phone = phone
		self.org_id = org_id
		self.group_id = group_id

	def __repr__(self):
		return "<User {}>".format(self.name)


class Profile(Base):
	__tablename__ = "profile"
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(80), nullable=False)
	description = Column(String(800))
	admin_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	# admin = relationship('User', backref=backref('profiles', lazy=True), cascade='delete')
	created = Column(DateTime, default=datetime.utcnow())
	updated = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


class UseType(Base):
	"""docstring for UseType"""
	__tablename__ = 'use_type'
	id = Column(Integer, primary_key=True, autoincrement=True)
	use_type = Column(String(30), nullable=False)
	created = Column(DateTime, default=datetime.utcnow())
	updated = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

	def __init__(self, use_type):
		self.use_type = use_type

	def __repr__(self):
		return "<UseType {}>".format(use_type)

# use_type options:
# 	0: free VARCHAR(255)
# 	1: INT
# 	2: float
# 	3: bool
# 	4: datetime
# 	5: email
# 	6: phone
# 	7: zipcode
# 	8: enum
# 	9: location


class CustomField(Base):
	"""docstring for CustomField"""
	__tablename__ = "custom_field"
	id = Column(Integer, primary_key=True, autoincrement=True)
	group_id = Column(Integer, ForeignKey('custom_field.id'))
	# group = relationship('CustomField', backref=backref('custom_field', lazy=True), cascade='delete')
	profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
	# profile = relationship('Profile', backref=backref('custom_fields', lazy=True), cascade='delete')
	name = Column(String(80), nullable=False)
	display_name = Column(String(80))
	multi_part = Column(Boolean, nullable=False, default=0)
	multi_use = Column(Boolean, nullable=False, default=0)
	use_type_id = Column(Integer, ForeignKey('use_type.id'), nullable=False, default=0)
	# use_type = relationship('UseType', backref=backref('custom_fields', lazy=True), cascade='delete')
	delim = Column(String(5), nullable=False, default=',')
	created = Column(DateTime, default=datetime.utcnow())
	updated = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

	def __init__(self, name, profile_id, group_id = None, display_name = None, multi_part = 0, multi_use = 0, use_type_id = 0, delim = ','):
		self.name = name
		self.profile_id = profile_id
		self.group_id = group_id
		self.display_name = display_name
		self.multi_part = multi_part
		self.multi_use = multi_use
		self.use_type_id = use_type_id
		self.delim = delim

	def __repr__(self):
		return "<CustomField {}>".format(self.name)

# multi_part options:
# 	0: no multi_part
# 	1: multi_part

# multi_use options:
# 	0: any
# 	1: all (requires delim, default is ',')

class Map(Base):
	"""docstring for Map"""
	__tablename__ = 'map'
	id = Column(Integer, primary_key=True, autoincrement=True)
	mls_id = Column(Integer, ForeignKey('mls.id'), nullable=False)
	# mls = relationship('MLS', backref=backref('maps', lazy=True), cascade='delete')
	resource_name = Column(String(80), nullable=False)
	class_name = Column(String(80), nullable=False)
	custom_field_id = Column(Integer, ForeignKey('custom_field.id'), nullable=False)
	# custom_field = relationship('CustomField', backref=backref('maps', lazy=True), cascade='delete')
	mls_field = Column(String(255), nullable=False)
	long_name = Column(String(80))
	searchable = Column(Boolean, nullable=False)
	lookup = Column(String(80))
	order = Column(SmallInteger, nullable=False, default=0)
	created = Column(DateTime, default=datetime.utcnow())
	updated = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

	def __init__(self, mls_id, resource_name, class_name, custom_field_id, mls_field, searchable, long_name = None, lookup = None, order = None):
		self.mls_id = mls_id
		self.resource_name = resource_name
		self.class_name = class_name
		self.custom_field_id = custom_field_id
		self.mls_field = mls_field
		self.searchable = searchable
		self.long_name = long_name
		self.lookup = lookup
		self.order = order

	def __repr__(self):
		return "<Map context {}:{}:{}:{}:{}>".format(self.mls_id, self.resource_name, self.class_name, self.custom_field_id, self.mls_field)
# ============================================================================== #


# ================================ CLI Handler ================================= #
if __name__ == "__main__":
	pass
# ============================================================================== #