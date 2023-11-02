set nocount on -- disable row affected message
DROP TABLE IF EXISTS #CustomerBasicData_Backup

CREATE TABLE #CustomerBasicData_Backup (
    CustomerID INT,
    AddressID INT,
    AddressType VARCHAR(20)
)

-- set start time for cursor
DECLARE @StartTimeCursor DATETIME;
SET @StartTimeCursor = GETDATE();

-- CURSOR VERSION
DECLARE c_customer_address CURSOR FOR SELECT CustomerID, AddressID, AddressType FROM SalesLT.CustomerAddress

DECLARE @customerID INT, @addressID INT, @address_type VARCHAR(20)

OPEN c_customer_address
FETCH NEXT FROM c_customer_address INTO @customerID, @addressID, @address_type
WHILE @@FETCH_STATUS = 0
BEGIN
    INSERT INTO #CustomerBasicData_Backup (CustomerID, AddressID, AddressType)
    VALUES (@customerID, @addressID, @address_type)
    FETCH NEXT FROM c_customer_address INTO @customerID, @addressID, @address_type
END
CLOSE c_customer_address

DEALLOCATE c_customer_address
-- set end time for cursor
DECLARE @EndTimeCursor DATETIME;
SET @EndTimeCursor = GETDATE();

-- calculate the difference in time in miliseconds
DECLARE @TimeElapsedCursor INT;
SET @TimeElapsedCursor = DATEDIFF(MILLISECOND, @StartTimeCursor, @EndTimeCursor);

-- display time
PRINT 'Cursor approach took ' + CAST(@TimeElapsedCursor AS NVARCHAR) + ' milliseconds.';

-- SELECT VERSION
DROP TABLE IF EXISTS #CustomerBasicData_Backupv2

CREATE TABLE #CustomerBasicData_Backupv2 (
    CustomerID INT,
    AddressID INT,
    AddressType VARCHAR(20)
)
-- set start timer for select approach
DECLARE @StartTimeSetBased DATETIME;
SET @StartTimeSetBased = GETDATE();

INSERT INTO #CustomerBasicData_Backupv2
SELECT CA.CustomerID, CA.AddressID, CA.AddressType
FROM SalesLT.CustomerAddress AS CA

-- set end time for select approach
DECLARE @EndTimeSetBased DATETIME;
SET @EndTimeSetBased = GETDATE();

-- count the time difference in miliseconds
DECLARE @TimeElapsedSetBased INT;
SET @TimeElapsedSetBased = DATEDIFF(MILLISECOND, @StartTimeSetBased, @EndTimeSetBased);

-- display the difference
PRINT 'Select based approach took ' + CAST(@TimeElapsedSetBased AS NVARCHAR) + ' milliseconds.';