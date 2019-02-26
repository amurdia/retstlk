-- =================================== Meta =====================================
-- Author: Ankit Murdia
-- Version: 0.0.1
-- Created: 2019-01-25 09:28:45
-- Updated: 2019-01-25 10:46:28
-- Description: SQLite setup
-- Notes:
-- To do:
-- ==============================================================================


-- ================================ Migrate up ==================================
DROP TABLE IF EXISTS mls;

CREATE TABLE mls (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	user TEXT NOT NULL,
	pass TEXT NOT NULL,
	useragent TEXT,
	useragentpass TEXT,
	rets_url TEXT,
	rets_ver TEXT,
	state TEXT NOT NULL,
	area_covered TEXT NOT NULL,
	association TEXT NOT NULL,
	broker TEXT NOT NULL,
	public_url TEXT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER mls_ts
BEFORE UPDATE ON mls FOR EACH ROW
BEGIN
	SET NEW.updated = CURRENT_TIMESTAMP
END;

CREATE TABLE organization (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	alias TEXT,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	phone TEXT,
	address TEXT,
	logo_url TEXT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER organization_ts
BEFORE UPDATE ON organization FOR EACH ROW
BEGIN
	SET NEW.updated = CURRENT_TIMESTAMP
END;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	alias TEXT,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	phone TEXT,
	org_id INTEGER,
	group_id INTEGER,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (group_id) REFERENCES user (id),
	FOREIGN KEY (org_id) REFERENCES organization (id)
);

CREATE TRIGGER user_ts
BEFORE UPDATE ON user FOR EACH ROW
BEGIN
	SET NEW.updated = CURRENT_TIMESTAMP
END;

CREATE TABLE profile (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	description TEXT,
	admin INTEGER NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (admin) REFERENCES user (id)
);

CREATE TRIGGER profile_ts
BEFORE UPDATE ON profile FOR EACH ROW
BEGIN
	SET NEW.updated = CURRENT_TIMESTAMP
END;

CREATE TABLE custom_field (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	group INTEGER,
	profile_id INTEGER NOT NULL,
	name TEXT NOT NULL,
	display_name TEXT NOT NULL,
	multi_part INTEGER NOT NULL DEFAULT 0,
	multi_use INTEGER NOT NULL DEFAULT 0,
	use_type INTEGER NOT NULL DEFAULT 0,
	delim TEXT TEXT NOT NULL DEFAULT ',',
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (group) REFERENCES custom_field (id),
	FOREIGN KEY (profile_id) REFERENCES profile (id)
);

-- multi_part options:
-- 	0: no multi_part
-- 	1: multi_part

-- multi_use options:
-- 	0: any
-- 	1: all (requires delim, default is ',')

-- use_type options:
-- 	0: free text
-- 	1: integer
-- 	2: float
-- 	3: bool
-- 	4: datetime
-- 	5: email
-- 	6: phone
-- 	7: zipcode
-- 	8: enum
-- 	9: location

CREATE TRIGGER custom_field_ts
BEFORE UPDATE ON custom_field FOR EACH ROW
BEGIN
	SET NEW.updated = CURRENT_TIMESTAMP
END;

CREATE TABLE map (
	mls_id INTEGER NOT NULL,
	resource TEXT NOT NULL,
	class TEXT NOT NULL,
	custom_field INTEGER NOT NULL,
	mls_field TEXT NOT NULL,
	long_name TEXT,
	searchable INTEGER NOT NULL DEFAULT 0,
	lookup TEXT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (mls_id) REFERENCES mls (id),
	FOREIGN KEY (custom_field) REFERENCES custom_fields (id)
);

CREATE TRIGGER map_ts
BEFORE UPDATE ON map FOR EACH ROW
BEGIN
	SET NEW.updated = CURRENT_TIMESTAMP
END;
-- ==============================================================================


-- =============================== Migrate down =================================

-- ==============================================================================
