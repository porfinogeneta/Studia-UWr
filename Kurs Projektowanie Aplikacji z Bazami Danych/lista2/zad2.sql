DROP TABLE IF EXISTS first_names;
CREATE TABLE first_names(
    ID INT PRIMARY KEY,
    FirstName VARCHAR(30)
    )
go

DROP TABLE IF EXISTS last_names;
CREATE TABLE last_names(
    ID INT PRIMARY KEY,
    LastName VARCHAR(30)
);
go

DROP TABLE IF EXISTS fldata;
CREATE TABLE fldata(
    [PKfirstname] VARCHAR(30),
    [PKlastname] VARCHAR(30) 
)
go

INSERT INTO last_names (ID, LastName) VALUES (1, 'Malinowski');
INSERT INTO last_names (ID, LastName) VALUES (2, 'Kowalski');
INSERT INTO last_names (ID, LastName) VALUES (3, 'Nowak');
INSERT INTO last_names (ID, LastName) VALUES (4, 'Ryba');

INSERT INTO first_names (ID, FirstName) VALUES (1, 'Kuba');
INSERT INTO first_names (ID, FirstName) VALUES (2, 'Zdzisław');
INSERT INTO first_names (ID, FirstName) VALUES (3, 'Marcin');
INSERT INTO first_names (ID, FirstName) VALUES (4, 'Artur');



DROP PROCEDURE if EXISTS fill_in_fldata
go

CREATE PROCEDURE fill_in_fldata @n int
as 
BEGIN

    -- determine if n exceeds maximal number of pairs
    -- crossjoin is better!
    IF (@n > (SELECT COUNT(*) FROM first_names) * (SELECT COUNT(*) FROM last_names))
    BEGIN
        THROW 500042, 'Possible pair number exceeded!', 1;
    END

    DROP TABLE IF EXISTS generated_pairs;
    CREATE TABLE generated_pairs(
        pair VARCHAR(5)
    );



    -- clear the table
    TRUNCATE TABLE fldata;
    -- populate table with data
    WHILE @n > 0
        BEGIN

            -- helper variables
            DECLARE @fst_name VARCHAR(20)
            DECLARE @fst_ID INT
            DECLARE @lst_name VARCHAR(20)
            DECLARE @lst_ID INT

            DECLARE @pair VARCHAR(20)

            -- get random name and its id
            SELECT TOP 1 @fst_name = [FirstName], @fst_ID = [ID]
            FROM first_names
            ORDER BY NEWID()

            -- get random last name and its id
            SELECT TOP 1 @lst_name = [LastName], @lst_ID = [ID]
            FROM last_names
            ORDER BY NEWID()

            SET @pair = CAST(@fst_ID AS VARCHAR(10))+ '-' + CAST(@lst_ID AS VARCHAR(10))

            -- could have checked only fldata
            -- if we have not selected such a pair, not in already generated
            IF NOT EXISTS (SELECT 1 FROM generated_pairs WHERE [pair] = @pair)
            BEGIN
                -- add to already generated
                INSERT INTO generated_pairs([pair])
                VALUES (@pair)

                -- add to you combined table
                INSERT INTO fldata([PKfirstname], [PKlastname])
                VALUES (@fst_name, @lst_name)

                -- reduce our n when the pair was founded
                SET @n = @n - 1
            END
        END
             
END
go

EXEC fill_in_fldata @n=16

SELECT * FROM fldata
