-- a script that prepares mysql server
-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- database to use
USE hbnb_test_db;
-- create user 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- set priviliges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privlige
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;