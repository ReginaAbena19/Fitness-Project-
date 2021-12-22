CREATE DATABASE Fitly;
use fitly;
CREATE TABLE login(
id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(100) NOT NULL,
email VARCHAR(500) NOT NULL,
Password1 VARCHAR(100) NOT NULL,
Password2 VARCHAR(100) NOT NULL
 ) ENGINE = InnoDB AUTO_INCREMENT =2 DEFAULT CHARSET = utf8;
 
 INSERT INTO login
(id, firstname, email, password1,password2)
VALUES
(001, 'Alixe','Alixecook@gmail.com','Strawberry','Strawberry'),
(002, 'Yasmine','Yasmineleghnider@gmail.com','Apple','Apple'),
(003, 'Delia','Delianeamtu-cucu@gmil.com','Fries','Fries'),
(004, 'Regina','Reginaob@gmail.com','Orange','Orange'),
(005, 'Raghad','Raghadzuraiki@gmail.com','Lemon','Lemon');


CREATE TABLE Youtube_results(
Workout_name VARCHAR(100) NOT NULL,
Workout_url VARCHAR(2048) NOT NULL
);

CREATE TABLE Exercise_db_results(
Workout_name VARCHAR(100) NOT NULL,
Exercise_goal Varchar(100) NOT NULL,
workout_demo_url VARCHAR(100) NOT NULL,
Location Varchar(100) NOT NULL
);

select*from login;


