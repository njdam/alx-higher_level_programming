-- A script that creates the database hbtn_0d_2 and the user user_0d_2.

-- Creating Database hbtn_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- You can insert this `USE hbtn_0d_2;` here or not
-- Creating User user_0d_2 if not exists with password user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Granting only SELECT privilege in database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Reload or Update or Apply(changes) all Privaleges from grant Tables
FLUSH PRIVILEGES;
