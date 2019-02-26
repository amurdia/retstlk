-- =================================== Meta =====================================
-- Author: Ankit Murdia
-- Version: 0.0.1
-- Created: 2019-01-25 09:28:45
-- Updated: 2019-01-25 10:46:28
-- Description: MySQL setup
-- Notes:
-- To do:
-- ==============================================================================


-- ================================ Migrate up ==================================
DROP TABLE IF EXISTS `mls`;
DROP TABLE IF EXISTS `organization`;
DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `profile`;
DROP TABLE IF EXISTS `custom_field`;
DROP TABLE IF EXISTS `map`;

CREATE TABLE mls (
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	user VARCHAR(255) NOT NULL,
	pass VARCHAR(255) NOT NULL,
	useragent VARCHAR(255),
	useragentpass VARCHAR(255),
	rets_url VARCHAR(255),
	rets_ver VARCHAR(255),
	state VARCHAR(255) NOT NULL,
	area_covered VARCHAR(255) NOT NULL,
	association VARCHAR(255) NOT NULL,
	broker VARCHAR(255) NOT NULL,
	public_url VARCHAR(255),
	created DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE organization (
	id INT AUTO_INCREMENT PRIMARY KEY,
	alias VARCHAR(255),
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	phone VARCHAR(255),
	address VARCHAR(255),
	logo_url VARCHAR(255),
	created DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
);

CREATE TABLE user (
	id INT AUTO_INCREMENT PRIMARY KEY,
	alias VARCHAR(20),
	name VARCHAR(80) NOT NULL,
	email VARCHAR(255) NOT NULL,
	phone VARCHAR(255),
	org_id INT,
	group_id INT,
	created DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (group_id) REFERENCES user(id) ON DELETE CASCADE,
	FOREIGN KEY (org_id) REFERENCES organization(id) ON DELETE CASCADE
);

CREATE TABLE profile (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(80) NOT NULL,
	description VARCHAR(800),
	admin INT NOT NULL,
	created DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (admin) REFERENCES user(id) ON DELETE CASCADE
);

CREATE TABLE use_type (
	id SMALLINT AUTO_INCREMENT PRIMARY KEY,
	type varchar(20) NOT NULL
);

-- use_type options:
-- 	0: free VARCHAR(255)
-- 	1: INT
-- 	2: float
-- 	3: bool
-- 	4: datetime
-- 	5: email
-- 	6: phone
-- 	7: zipcode
-- 	8: enum
-- 	9: location

CREATE TABLE custom_field (
	id INT AUTO_INCREMENT PRIMARY KEY,
	group INT,
	profile_id INT NOT NULL,
	name VARCHAR(80) NOT NULL,
	display_name VARCHAR(80) NOT NULL,
	multi_part BIT NOT NULL DEFAULT 0,
	multi_use BIT NOT NULL DEFAULT 0,
	use_type_id SMALLINT NOT NULL DEFAULT 0,
	delim VARCHAR(5) NOT NULL DEFAULT ',',
	created DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (group) REFERENCES custom_field(id) ON DELETE CASCADE,
	FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE,
	FOREIGN KEY (use_type_id) REFERENCES use_type(id) ON DELETE CASCADE
);

-- multi_part options:
-- 	0: no multi_part
-- 	1: multi_part

-- multi_use options:
-- 	0: any
-- 	1: all (requires delim, default is ',')

CREATE TABLE map (
	mls_id INT NOT NULL,
	resource VARCHAR(80) NOT NULL,
	class VARCHAR(80) NOT NULL,
	custom_field INT NOT NULL,
	mls_field VARCHAR(80) NOT NULL,
	long_name VARCHAR(80),
	searchable BIT NOT NULL DEFAULT 0,
	lookup VARCHAR(80),
	created DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (mls_id) REFERENCES mls(id) ON DELETE CASCADE,
	FOREIGN KEY (custom_field) REFERENCES custom_fields(id) ON DELETE CASCADE
);

-- ==============================================================================


-- =============================== Migrate down =================================

-- ==============================================================================
