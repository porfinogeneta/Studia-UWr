CEATE DATABASE Z1;
USE Z1;

DROP TABLE IF EXISTS OSOBA

-- A surrogate key is defined as a unique identifier for some record or object in a table.
-- It is similar to a primary key, but with a significant difference: it is not derived from
-- the table data – the object generates this key itself.

-- DEFAULT sprawia ze mona swoje id dodawac

CREATE TABLE OSOBA (
    ID INT AUTO_INCEREMENT PRIMARY KEY,
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