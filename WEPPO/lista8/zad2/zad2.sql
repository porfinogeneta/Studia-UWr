CREATE DATABASE Z2;


DROP TABLE IF EXISTS OSOBA;


CREATE TABLE OSOBA (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(30),
    SURNAME VARCHAR(30),
    SEX VARCHAR(10),
    AGE INT,
    SALARY DECIMAL(10,2)
);


INSERT INTO OSOBA (NAME, SURNAME, SEX, AGE, SALARY)
VALUES  
    ('John', 'Doe', 'Male', 25, 50000.00),
    ('Jane', 'Smith', 'Female', 30, 60000.50);