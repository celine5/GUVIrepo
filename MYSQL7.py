CREATE DATABASE bird;
USE bird;
CREATE TABLE Employee(id int NOT NULL AUTO_INCREMENT,
name varchar(12) NOT NULL,
age int(2) NOT NULL,
PRIMARY KEY (id)
);
INSERT INTO Employee(id,name,age) VALUES(1,"Vinodini",25);
INSERT INTO Employee(id,name,age) VALUES(2,"Banu",27);
INSERT INTO Employee(id,name,age) VALUES(3,"kaushik",23);
INSERT INTO Employee(id,name,age) VALUES(4,"Praveen",25);
INSERT INTO Employee(id,name,age) VALUES(5,"Kamal",22);
INSERT INTO Employee(id,name,age) VALUES(6,"Malini",24);
INSERT INTO Employee(id,name,age) VALUES(7,"Ramesh",32);
SELECT * FROM Employee;
