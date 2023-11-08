USE AdventureWorksLT2022

DROP TABLE IF EXISTS dbo.ProductCost
GO

-- tabelka ze wszystkimi zmianami cen danego produktu
CREATE TABLE dbo.ProductCost (
    -- CostID INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT,
    StandardCost DECIMAL(10, 2),
    ListPrice DECIMAL(10, 2),
    ModifiedDate DATETIME,
)
GO

-- dodanie wejściowych wartości do ProductCost
INSERT INTO dbo.ProductCost (ProductID, StandardCost, ListPrice, ModifiedDate)
SELECT P.ProductID, P.StandardCost, P.ListPrice, P.ModifiedDate
FROM SalesLT.Product AS P
GO