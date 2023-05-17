-- Task: Create MySQL server user user_0d_1
-- CREATE USER query to create the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- GRANT query to give the user all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- End of the script

