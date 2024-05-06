-- Create a new database with name 'hbnb_dev_db'
-- Create a new user 'hbn_dev' with different  privileges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db

CREATE USER IF NOT EXISTS 'hbnb_dev'@''localhost' IDENTIFIED BY 'hbn_dev_pwd

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
