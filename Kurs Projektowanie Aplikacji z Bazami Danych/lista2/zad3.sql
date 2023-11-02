DROP PROCEDURE IF EXISTS add_new_reader;
GO

CREATE PROCEDURE add_new_reader @PESEL VARCHAR(11), @last_name VARCHAR(30), @city VARCHAR(30), @birth VARCHAR(30)
AS
BEGIN
    -- PESEL validation
    IF LEN(@PESEL) <> 11 OR ISNUMERIC(@PESEL) = 0
    BEGIN
        THROW 50042, 'Invalid PESEL', 1;
    END
    
    -- last_name vaidation
    IF LEN(@last_name) < 2 OR
     (LEFT(UPPER(@last_name) COLLATE Latin1_General_BIN, 1)
     <> LEFT(@last_name COLLATE Latin1_General_BIN, 1))
    BEGIN
        THROW 50044, 'Invalid Last Name', 2;
    END
      

    -- check date format (our format is 23 - YYYY-MM-DD)
    -- we use try/catch so we can catch all runtime errors
    BEGIN TRY
        SET @birth = FORMAT(CAST(@birth AS DATE), 'yyyy-MM-dd');
    END TRY
    BEGIN CATCH
        THROW 50045, 'Invalid Date Format (YYYY-MM-DD)', 3;
        RETURN;
    END CATCH

    -- -- if data is valid insert new Czytelnik
    INSERT INTO Czytelnik
        ([PESEL], [Nazwisko], [Miasto], [Data_Urodzenia]) VALUES
        (@PESEL, @last_name, @city, @birth)

END

-- every parameter is correct
-- go
-- EXEC add_new_reader @PESEL = '11113211111', @last_name='Kazimierczak', @city='Wroclaw', @birth='2000-12-20';
-- go

--check na pesel
-- go
-- EXEC add_new_reader @PESEL = '11a11211111', @last_name='Zkk', @city='Wroclaw', @birth='2000-12-20';
-- go

-- check last name

-- for special characters
-- go
-- EXEC add_new_reader @PESEL = '21111211111', @last_name='Źą', @city='Wroclaw', @birth='2000-12-20';
-- go
-- for small letters
-- go
-- EXEC add_new_reader @PESEL = '11111211311', @last_name='kaz', @city='Wroclaw', @birth='2000-12-20';
-- go
-- for one letter
-- go
-- EXEC add_new_reader @PESEL = '11111211311', @last_name='k', @city='Wroclaw', @birth='2000-12-20';
-- go

-- check date
go
EXEC add_new_reader @PESEL = '11724212311', @last_name='Kaz', @city='Wroclaw', @birth='2000-22-31';
go