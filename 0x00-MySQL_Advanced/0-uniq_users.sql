-- A script that creates a users table
-- Create table syntax with constraints
CREATE TABLE users (
  id int NOT NULL AUTO_INCREMENT,
  email varchar(255) NOT NULL,
  name varchar(255),
  PRIMARY KEY (id),
  CONSTRAINT user_email UNIQUE(email)
);