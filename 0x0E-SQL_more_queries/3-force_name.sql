-- A script that creates the table force_name on your MySQL server.

-- Creating force_name if not exists with id, and name shouldn't be NULL
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
