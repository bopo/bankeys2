PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL
);
INSERT INTO "alembic_version" VALUES('b9ff5977caa5');
CREATE TABLE goods (
	id INTEGER NOT NULL, 
	g_name VARCHAR, 
	g_price VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE sign (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	password VARCHAR, 
	req_id VARCHAR, 
	appkey VARCHAR, 
	is_ok BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (req_id), 
	CHECK (is_ok IN (0, 1))
);

CREATE TABLE user (
	id INTEGER NOT NULL, 
	name VARCHAR(128), 
	PRIMARY KEY (id)
);
CREATE TABLE orders (
	id INTEGER NOT NULL, 
	order_num VARCHAR, 
	good_id INTEGER, 
	drawee VARCHAR, 
	address VARCHAR, 
	g_name VARCHAR, 
	g_price VARCHAR, 
	mobile VARCHAR, 
	g_type VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(good_id) REFERENCES goods (id), 
	UNIQUE (address), 
	UNIQUE (order_num)
);

CREATE INDEX ix_goods_id ON goods (id);
CREATE INDEX ix_sign_id ON sign (id);
COMMIT;
