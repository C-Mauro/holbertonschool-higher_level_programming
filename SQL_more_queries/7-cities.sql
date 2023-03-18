-- create a database and a table 

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL FOREING KEY (state_id) REFERENCES hbtn_0d_usa.state(id),
	name VARCHAR(256) NOT NULL
);
