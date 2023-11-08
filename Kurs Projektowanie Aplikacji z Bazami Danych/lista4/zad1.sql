USE AdventureWorksLT2022
GO


DROP TRIGGER IF EXISTS SalesLT.tr_modified_date;  
GO

CREATE TRIGGER SalesLT.tr_modified_date ON SalesLT.Customer AFTER UPDATE
AS 
BEGIN
    UPDATE C
    SET C.ModifiedDate = GETDATE()
    FROM SalesLT.Customer AS C
    INNER JOIN INSERTED AS I 
    ON I.CustomerID = C.CustomerID
    INNER JOIN DELETED AS D
    ON D.CustomerID = C.CustomerID    
END
GO



UPDATE SalesLT.Customer
SET FirstName = 'KrlanDo'
WHERE CustomerID = 1
GO
