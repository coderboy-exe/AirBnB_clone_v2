-- Prepare a MySQL server for the project
-- GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- Create the hbnb_dev_db database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the hbnb_dev user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush Privileges
FLUSH PRIVILEGES;
