CREATE DATABASE FITLY_USERS
USE fitly_users;


CREATE TABLE USERS(
User_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Username VARCHAR(100) NOT NULL,
User_password VARCHAR(100) NOT NULL,
User_email VARCHAR(100) NOT NULL
 ) ENGINE = InnoDB AUTO_INCREMENT =2 DEFAULT CHARSET = utf8;

Select*from users;
