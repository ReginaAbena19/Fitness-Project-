CREATE DATABASE VIDEOS;
USE videos;


CREATE TABLE LEGS(
Legs_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Workout_name VARCHAR(100) NOT NULL,
Workout_url VARCHAR(2048) NOT NULL,
Exercise_goal Varchar(100) NOT NULL,
Location Varchar(100) NOT NULL
 );
 

INSERT INTO LEGS
(Legs_id, workout_name, workout_url,exercise_goal,location)
VALUES
(1, '45 min best glutes workout for women', 'https://youtu.be/bTEoN2ULzwg', 'Endurance','Home'),
(2, 'Perfect Leg Workout', 'https://youtu.be/AQyhNSDXYf0', 'Strength Training','Gym'),
(3, 'Slim legs', 'https://youtu.be/Jg61m0DwURs', 'Weightloss','Home'),
(4, 'Lower body HIIT Workout','https://youtu.be/8-PjpUH8TcE','Cardio','Home'),
(5, 'Fire Legs and Booty Workout','https://youtu.be/EaWPDMOqiBQ','Strength Training','Gym'),
(6, 'Intense Full Booty Workout','https://youtu.be/_9WPJ8ffHus','Endurance','Gym'),
(7, 'Booty Workout','https://youtu.be/ZeZfgyMXk34','Strength Training','Gym'),
(8, 'Booty and Hamstring Workout','https://youtu.be/OSsYLsQJ-D8','Strength Training','Gym'),
(9, 'Five must do Glutes Exercises','https://youtu.be/6vlP9xPJbaQ','Strength Training','Gym'),
(10, 'Twenty minute Booty Workout','https://youtu.be/dy_ExlCUckQ','Endurance','Home'),
(11, 'Dumbbell Only Booty and Leg Workout','https://youtu.be/3OUgkLNfCzg','Strength Training','Home'),
(12, 'Dumbbell Booty Workout','https://youtu.be/znoxbp2yY8M','Strength Training','Home'),
(13, 'Slimmer legs Workout','https://youtu.be/nSECUu4VFOc','Weightloss','Home'),
(14, 'Legs and Fatburn Workout','https://youtu.be/R1EKAgFRe2E','Weightloss','Home'),
(15, 'Burn Thigh Fat Workout','https://youtu.be/StN0-7XLuR4','Cardio','Home'),
(16, 'Intense Glutes Workout','https://youtu.be/p_azB88VSwE','Strength Training','Gym'),
(17, 'Booty Burn Workout','https://youtu.be/bggX6ocjojk','Endurance','Home'),
(18, 'Slimmer Inner Thighs and Legs Workout','https://youtu.be/zLBFQ_mFl2E','Weightloss','Home'),
(19, 'Killer Leg Day Workout','https://youtu.be/eemRXHKsGIc','Strength Training','Gym'),
(20, 'Gym Killer Booty Workout','https://youtu.be/Y5_PhinwXKo','Strength Training','Gym'),
(21, 'Strong Glutes and Toned Thighs Workout','https://youtu.be/4c8mNETuCcg','Strength Training','Gym'),
(22, 'Lower body strength Workout','https://youtu.be/MjPVPDBJ94A','Endurance','Home'),
(23, 'Lower impact HIIT leg cardio Workout','https://youtu.be/tb7dWAOy7zo','Cardio','Home'),
(24, 'Lower body burn Workout','https://youtu.be/X_sr8gy2cNE','Strength Training','Home'),
(25, 'Legs slimming cardio pilates Workout','https://youtu.be/KpCPgNer_Oo','Cardio','Home'),
(26, 'Strength your Legs  Workout','https://youtu.be/AqMIw-L9LcY','Cardio','Home'),
(27, 'Legs and Glutes Cardio Workout','https://youtu.be/fkL15qFiXBQ','Endurance','Home'),
(28, 'Legs, Glutes and Thighs Workout','https://youtu.be/sSiq1opmejo','Endurance','Home'),
(29, 'Glutes and Thighs Workout','https://youtu.be/oJs7hzlHWco','Weightloss','Home'),
(30, 'Leg Fat Burn Workout','https://youtu.be/572LqIkcsOk','Weightloss','Home');



Select*from legs;


CREATE TABLE ARMS(
Arms_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Workout_name VARCHAR(100) NOT NULL,
Workout_url VARCHAR(2048) NOT NULL,
Exercise_goal Varchar(100) NOT NULL,
Location Varchar(100) NOT NULL
 );
 
INSERT INTO ARMS
(Arms_id, workout_name, workout_url,exercise_goal,Location)
VALUES
(1, 'HITT Arms', 'https://youtu.be/8BRfLyQ9DMg', 'Endurance','Home'),
(2, 'Toned Arms Workout', 'https://youtu.be/l0CwCvJbGZI', 'Strength Training','Home'),
(3, 'Lose Arm Fat', 'https://youtu.be/Qq_KB5z2-os', 'Weightloss','Home'),
(4, 'Leans Arm Cardio Workout', 'https://youtu.be/Ai8KfyJ69Bc', 'Cardio','Home'),
(5, '30 min upper body Workout','https://youtu.be/rOf4tRtuvyA','Cardio','Home'),
(6, '5 min arm and back fat Workout','https://youtu.be/nJZe9nLWv7A','Cardio','Home'),
(7, '10 min toned arms Workout','https://youtu.be/j64BBgBGNIU','Endurance','Home'),
(8, 'Tone your arms Workout','https://youtu.be/UyTR2EjTAXU','Endurance','Home'),
(9, '40 minute cardio and arms Workout','https://youtu.be/738IcvTnII4','Endurance','Home'),
(10, 'Fat burning Tank top arms Workout','https://youtu.be/TSDS8KixaQ0','Cardio','Home'),
(11, '4-minute no-weight, arm toning Workout','https://youtu.be/PJO1hQSMPT4','Cardio','Home'),
(12, '30-minute no-equipment arms and abs Workout','https://youtu.be/g1E2Tasqog4','Endurance','Home'),
(13, '30-min arm workout with dummbbells Workout','https://youtu.be/AuLJr3e3ruY','Strength Training','Home'),
(14, 'Full biceps and triceps workout for bigger arms','https://youtu.be/J7buRPxIY1c','Strength Training','Gym'),
(15, 'Target your entire upperbody Workout','https://youtu.be/akNXWdYg0tw','Strength Training','Gym'),
(16, 'Arm day Workout','https://youtu.be/bXItN5LESkw','Endurance','Gym'),
(17, 'Strong and lean arms Workout','https://youtu.be/cWfjld3fV48','Strength Training','Gym'),
(18, 'Quick dumbbell only upperbody Workout','https://youtu.be/J3i3oxyNn9M','Endurance','Gym'),
(19, 'Complete arm Workout','https://youtu.be/4dCn9VrFlEY','Strength Training','Gym'),
(20, 'Beginner Arm Workout','https://youtu.be/FSoI9y6k_ZU','Strength Training','Gym'),
(21, 'Target biceps and triceps Workout','https://youtu.be/bl_ZSXldBrU','Strength Training','Gym'),
(22, 'Full biceps and triceps Workout','https://youtu.be/3vw0w_j7O1A','Strength Training','Gym'),
(23, 'Arm day Workout- biceps and triceps','https://youtu.be/zmJn5Hwhf8U','Endurance','Gym'),
(24, 'Beginners toned arms Workout','https://youtu.be/8sztlPxl0MQ','Endurance','Home'),
(25, 'Arm day-best arm exercises Workout','https://youtu.be/6_hfafaneag','Strength Training','Gym'),
(26, '15 min arm workout(Dumbbells only)','https://youtu.be/UY6-JzdnHUM','Strength Training','Gym'),
(27, 'Beginners Upper Body Workout','https://youtu.be/Ef269tdwbrE','Endurance','Gym'),
(28, 'Back and Shoulder Workout','https://youtu.be/fRnwshs58m0','Strength Training','Gym'),
(29, '13 best exercises for bigger arms Workout','https://youtu.be/LHBINS08Yy0','Strength Training','Gym'),
(30, ' Beginner upper body arm Workout','https://youtu.be/m6XAnp7o3Ys','Strength Training','Gym');

CREATE TABLE ABS(
Abs_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Workout_name VARCHAR(100) NOT NULL,
Workout_url VARCHAR(2048) NOT NULL,
Exercise_goal Varchar(100) NOT NULL,
Location Varchar(100) NOT NULL
 );
 
 
 INSERT INTO ABS
(Abs_id, workout_name, workout_url,exercise_goal,location)
VALUES
(1, 'Intense Cardio Abs Workout', 'https://youtu.be/3gGs1DZsFeI', 'Endurance','Home'),
(2, 'Dumbbell Abs Workout', 'https://youtu.be/mUI4hXTmAkw', 'Strength Training','Home'),
(3, 'Belly Fat Burner', 'https://youtu.be/owrBD7_8edA', 'Weightloss','Home'),
(4, 'Cardio Abs Workout', 'https://youtu.be/WlLZu_57jQY', 'Cardio','Home'),
(5, 'Six-minute Abs Workout','https://youtu.be/r9BvRoAZEJ4','Endurance','Home'),
(6, 'Fully Body Workout','https://youtu.be/3Vh6PH5L_GE','Cardio','Home'),
(7, 'Dumbbell Booty and Abs Workout','https://youtu.be/znoxbp2yY8M','Strength Training','Home'),
(8, 'Five minute Abs Workout','https://youtu.be/0UgAUJxqvUU','Cardio','Home'),
(9, 'Sculpt It Workout','https://youtu.be/YDfKRnGssX0','Cardio','Home'),
(10, 'Abdominal Endurance challenge','https://youtu.be/KGdu6vdKIUM','Endurance','Home'),
(11, '10 min home workout for 6pack','https://youtu.be/ofTiKY3hYdE','Endurance','Home'),
(12, '20 min total core Workout','https://youtu.be/-b2lNLq3EaA','Endurance','Home'),
(13, 'The perfect Abs Workout','https://youtu.be/qk97w6ZmV90','Cardio','Gym'),
(14, '10 min runner core endurance Workout','https://youtu.be/HmZJVQEA0ts','Endurance','Home'),
(15, '30 min abs Workout','https://youtu.be/P1mInEK7BEU','Cardio','Home'),
(16, 'Intense 10 min Abdominal Strength Workout','https://youtu.be/6XvIGaJ3Ns4','Endurance','Home'),
(17, 'Best Home Ab Workout','https://youtu.be/zzD80vCLq0Y','Cardio','Home'),
(18, 'Blast fitness endurance HIIT Workout','https://youtu.be/xykd5XHosrQ','Endurance','Home'),
(19, '20 min fat burning cardio and abs Workout','https://youtu.be/8ortypveAL0','Cardio','Home'),
(20, '12 min intense cardio abs and core Workout','https://youtu.be/Fy7ZbhxLEPo','Cardio','Home'),
(21, '10 min cardio abs Workout','https://youtu.be/EoxQKyYTQA0','Cardio','Home'),
(22, '30 min cardio and core Workout','https://youtu.be/05fCNM9f0ic','Cardio','Home'),
(23, 'Crazy HIIT Workout cardio and abs','https://youtu.be/9aaPze7LqUw','Cardio','Home'),
(24, 'Intense cable only Abs Workout','https://youtu.be/1XBQMd1Q9tc','Strength Training','Gym'),
(25, 'Abs core routine Workout','https://youtu.be/UxeGP2sYedM','Strength Training','Gym'),
(26, 'Intense Abs Workout for fire core','https://youtu.be/b5tXfecmtjE','Strength Training','Gym'),
(27, 'Complete Ab Workout','https://youtu.be/iQIrxBmgXmE','Strength Training','Gym'),
(28, 'Quick Gym based Ab Workout','https://youtu.be/DNPKbHFfjx8','Strength Training','Gym'),
(29, 'Quick Easy Cardio and Ab Workout','https://youtu.be/BRv5t8MHRzs','Strength Training','Gym'),
(30, 'After Christmas Glutes and Ab Workout','https://youtu.be/sg342JzSylk','Strength Training','Gym');


 CREATE TABLE BACK(
back_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Workout_name VARCHAR(100) NOT NULL,
Workout_url VARCHAR(2048) NOT NULL,
Exercise_goal Varchar(100) NOT NULL,
Location Varchar(100) NOT NULL
 );
 
 INSERT INTO BACK
(Back_id, workout_name, workout_url,exercise_goal,location)
VALUES
(1, 'Leaner Back', 'https://youtu.be/MB3A1lh23cQ', 'Endurance','Home'),
(2, '5 Must do Back exercises', 'https://youtu.be/twjhKJtHwfg', 'Strength Training','Gym'),
(3, 'Loose Back Fat', 'https://youtu.be/MC3bV56np4I', 'Weightloss','Home'),
(4, 'Cardio and Back Workout', 'https://youtu.be/7AZVlOX6lWM', 'Cardio','Home'),
(5, 'Intense Back Workout','https://youtu.be/RxGvauKniUY','Strength Training','Gym'),
(6, 'Five must do back exercises for waist','https://youtu.be/ziFsDzn7RGk','Strength Training','Gym'),
(7, 'Snatch your back full Workout','https://youtu.be/4IyMwqMBC9A','Strength Training','Gym'),
(8, 'Reduce upperbody fat Workout','https://youtu.be/vj7vuf2Itt4','Cardio','Home'),
(9, 'Back Fat Blaster Workout','https://youtu.be/T9AlsZwPwG0','Cardio','Home'),
(10, 'Burn fat-lower back and waist slimmer Workout','https://youtu.be/LkXVLxYbPk0','Cardio','Home'),
(11, '10 min Back and Arms Workout','https://youtu.be/Mh_3ddy9zbY','Cardio','Home'),
(12, '20 min home back Workout','https://youtu.be/14LTcAIwBoI','Cardio','Home'),
(13, '5 min burn back fat workout with dumbbells','https://youtu.be/oVbgdI-zGGw','Cardio','Home'),
(14, 'Bra bulge and back fat Workout','https://youtu.be/qqHJLTi2yX4','Cardio','Home'),
(15, 'Back and biceps muscular endurance Workout','https://youtu.be/QTBS-fWExFQ','Cardio','Gym'),
(16, '15 min bounce-back cardio dance Workout','https://youtu.be/Rj2IubFfEqY','Cardio','Home'),
(17, 'Upper body fat burning superset Workout','https://youtu.be/j7HnFtNmDl4','Cardio','Home'),
(18, '10 min intense back Workout','https://youtu.be/1dJ-d7tVwEk','Cardio','Home'),
(19, 'Best science-based back Workout','https://youtu.be/8LJ3Q3Fsrzs','Strength Training','Gym'),
(20, '20 min back Workout ','https://youtu.be/BTwHPYm-16Y','Strength Training','Gym'),
(21, 'Intense Back Workout','https://youtu.be/9UQ71kFRudI','Endurance','Home'),
(22, 'Intense back and bra bulge burn Workout','https://youtu.be/30zuVLLvy5I','Cardio','Home'),
(23, '12 min upper body Workout','https://youtu.be/B3Y5kYDH-Mo','Cardio','Home'),
(24, '9 exercises to build a big back Workout','https://youtu.be/s8taXR3mYa8','Strength Training','Home'),
(25, 'The perfect back workout Workout','https://youtu.be/eE7dzM0iexc','Strength Training','gym'),
(26, '20 min dumbbell back workout Workout','https://youtu.be/cMUP-Z8dG9A','Strength Training','gym'),
(27, 'Sculpted Back and Defined Shoulders Workout','https://youtu.be/ddL27T3152Q','Strength Training','Gym'),
(28, 'Back and Biceps Workout','https://youtu.be/ET1E_7aauzg','Strength Training','Gym'),
(29, '10 min Upper body Workout','https://youtu.be/ranPUb8Tzwk','Strength Training','Home'),
(30, 'Beginner Back Workout','https://youtu.be/Fqg-jPvjlS4','Strength Training','Gym');

