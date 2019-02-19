CREATE DATABASE bird;
USE bird;
CREATE TABLE student(id int(1) NOT NULL,name varchar(15) NOT NULL,city varchar(14));
INSERT INTO student(id,name,city) VALUES(1,"celine","chennai");
INSERT INTO student(id,name,city) VALUES(2,"cesi","ooty");
INSERT INTO student(id,name,city) VALUES(3,"annie","theni");
SELECT COUNT(*)FROM student;
SELECT DISTINCT name FROM student;
