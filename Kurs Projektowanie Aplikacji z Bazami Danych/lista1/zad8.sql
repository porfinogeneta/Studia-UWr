-- podgląd wszystkich ograniczeń
-- SELECT OBJECT_NAME(object_id) AS TableName, name AS ConstraintName, definition AS CheckConstraint
-- FROM sys.check_constraints
-- WHERE OBJECT_NAME(parent_object_id) = 'SalesOrderHeader';

-- CK_SalesOrderHeader_ShipDate	CK_SalesOrderHeader_ShipDate	([ShipDate]>=[OrderDate] OR [ShipDate] IS NULL)

-- DISABLE CONSTRAINT
ALTER TABLE [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader] NOCHECK CONSTRAINT CK_SalesOrderHeader_ShipDate


-- update na nie działające
UPDATE [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader]
SET
    [RevisionNumber] = 3,
    [OrderDate] = '2008-06-20 00:00:00.000',
    [DueDate] = '2008-06-14 00:00:00.000',
    [ShipDate] = '2008-06-09 00:00:00.000'
WHERE [SalesOrderID] = 71774;

-- VIOLATION
-- The UPDATE statement conflicted with the CHECK constraint "CK_SalesOrderHeader_DueDate". 
-- The conflict occurred in database "AdventureWorksLT2022", table "SalesLT.SalesOrderHeader".

-- ponowne uruchomienie ograniczenia
ALTER TABLE [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader] CHECK CONSTRAINT CK_SalesOrderHeader_ShipDate

--DBCC check_constraints do wylistowania ograniczeń

-- kiedy mamy violation
SELECT *
FROM [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader]
WHERE [ShipDate] < [OrderDate];

