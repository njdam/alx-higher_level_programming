-- A script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.

-- Creation of Database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creation of table cities if not exists with unique id, state_id as
-- FOREIGN KEY references from state id and name which are not NULL
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL);
