-- create database, user and set privileges
-- prepares mysql server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- use database
USE hbnb_dev_db;
-- creates db if it doen't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grants privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- grants select prievilidges to perfomance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;