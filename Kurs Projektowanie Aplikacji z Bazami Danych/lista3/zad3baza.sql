DROP TABLE IF EXISTS Prices;
GO

DROP TABLE IF EXISTS Products;
GO

DROP TABLE IF EXISTS Rates;
GO

-- Create Products table
CREATE TABLE Products (
    ID INT IDENTITY PRIMARY KEY,
    ProductName VARCHAR(255)
);

-- Create Rates table
CREATE TABLE Rates (
    Currency VARCHAR(3) PRIMARY KEY,
    PricePLN DECIMAL(10, 2)
);

-- Create Prices table with foreign keys
CREATE TABLE Prices (
    ProductID INT REFERENCES Products(ID),
    Currency VARCHAR(3) REFERENCES Rates(Currency),
    Price DECIMAL(10, 2) NOT NULL,
);

-- Insert data into Products
SET IDENTITY_INSERT Products ON
INSERT INTO Products (ID, ProductName)
VALUES
    (1, 'Product 1'),
    (2, 'Product 2'),
    (3, 'Product 3'),
    (4, 'Product 4');
SET IDENTITY_INSERT Products OFF

-- Insert data into Rates
INSERT INTO Rates (Currency, PricePLN)
VALUES
    ('USD', 4.00),
    ('EUR', 4.50),
    ('GBP', 5.00),
    ('PLN', 1.00),
    ('CHF', 4.40);
    

-- Insert data into Prices
INSERT INTO Prices (ProductID, Currency, Price)
VALUES
    (1, 'PLN', 40.00),
    
    (2, 'PLN', 15.00),
    (1, 'EUR', 10.50),
    (3, 'PLN', 20.00),
    (2, 'GBP', 90.00),
    (4, 'PLN', 48.00),
    (4, 'CHF', 48.00);

SELECT *
FROM Prices
ORDER BY
    ProductID ASC, -- Sort by ProductID in ascending order
    CASE
        WHEN Currency = 'PLN' THEN 1 -- 'PLN' comes first
        ELSE 2 -- All other currencies come after 'PLN'
    END,
    Currency ASC; -- Sort the currencies in ascending order within each group
