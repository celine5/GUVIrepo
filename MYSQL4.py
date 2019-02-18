CREATE TABLE myfriends
(
    last_name   VARCHAR(15) NOT NULL,
    first_name  VARCHAR(15) NOT NULL,
    suffix      VARCHAR(5) NULL,
    sex         VARCHAR(1) NULL,
    city        VARCHAR(20) NOT NULL,
    state       VARCHAR(2) NOT NULL,
    age     int
);

ALTER TABLE myfriends ADD ROLLNUMBER SMALLINT UNSIGNED;

ALTER TABLE myfriends ADD INDEX(ROLLNUMBER);

DESCRIBE myfriends;

DROP TABLE myfriends;
