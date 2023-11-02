DROP PROCEDURE IF EXISTS set_discontinued_date;

DROP TYPE IF EXISTS ProductTableListType;
GO

CREATE TYPE ProductTableListType AS TABLE (
    ID INT
)
GO


CREATE PROCEDURE set_discontinued_date @product_ids ProductTableListType READONLY, @change_date DATE
AS
BEGIN
    -- helper table to store already modyfied
    DROP TABLE IF EXISTS #updated
    CREATE TABLE #updated([ID] INT);

    -- updated is a table with already changed Discontinued Column
    INSERT INTO #updated
    SELECT P.ProductID 
    FROM [AdventureWorksLT2022].[SalesLT].Product AS P
    WHERE P.DiscontinuedDate IS NOT NULL

    -- print appropriate message for modified
    DECLARE @help INT;
    WHILE (SELECT COUNT(*) FROM #updated) > 0
    BEGIN
        SELECT TOP 1 @help = [ID] from #updated
        PRINT 'Cannot be updated ' + CAST(@help AS VARCHAR(10))
        DELETE FROM #updated WHERE [ID] = @help
    END

    UPDATE P
    SET P.DiscontinuedDate = @change_date
    FROM [AdventureWorksLT2022].[SalesLT].[Product] AS P
    INNER JOIN @product_ids AS PD
    ON PD.ID = P.ProductID
    WHERE P.DiscontinuedDate IS NULL


END

GO
DECLARE @table ProductTableListType;

INSERT INTO @table([ID]) VALUES (680), (706), (707), (708)
exec set_discontinued_date @product_ids=@table, @change_date='2020-01-10'
GO