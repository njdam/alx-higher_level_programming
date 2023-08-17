-- A script that creates the table id_not_null on your MySQL server.

-- Creation of id_not_null table with id which is not NULL and name
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
