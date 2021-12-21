Create Database Fitly
use fitly;
CREATE TABLE login(
id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL
 ) ENGINE = InnoDB AUTO_INCREMENT =2 DEFAULT CHARSET = utf8;
 
 INSERT INTO login
(id, firstname, email, password)
VALUES
(001, 'Alixe','Alixecook@gmail.com','Stawberry'),
(002, 'Yasmine','Yasmineleghnider@gmail.com','Apple'),
(003, 'Delia','Delianeamtu-cucu@gmil.com','Fries'),
(004, 'Regina','Reginaob@gmail.com','Orange'),
(005, 'Raghad','Raghadzuraiki@gmail.com','Lemon');


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
