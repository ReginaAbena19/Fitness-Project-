
USE fitly_users;


CREATE TABLE USERS(
User_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Username VARCHAR(100) NOT NULL,
User_password VARCHAR(100) NOT NULL,
User_email VARCHAR(100) NOT NULL
 ) ENGINE = InnoDB AUTO_INCREMENT =2 DEFAULT CHARSET = utf8;

Select*from users;

CREATE TABLE YOUTUBE_RESULTS(
Workout_name VARCHAR(100) NOT NULL,
Workout_url VARCHAR(2048) NOT NULL
);

CREATE TABLE EXERCISE_DB_WORKOUTS(
Workout_name VARCHAR(100) NOT NULL,
Exercise_goal Varchar(100) NOT NULL,
workout_demo_url VARCHAR(100) NOT NULL,
Location Varchar(100) NOT NULL
);




