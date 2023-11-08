DROP TRIGGER IF EXISTS tr_access_website
GO

DROP TRIGGER IF EXISTS tr_access_history
GO

CREATE TRIGGER tr_access_history ON dbo.History
INSTEAD OF INSERT
AS
BEGIN
    -- SELECT * FROM inserted
    -- jeżeli próbujemy dodać coś co już było w dbo.History, zmieniamy tylko LatestAccess
    DECLARE @id INT
    SET @id = (SELECT ID from inserted)

    DECLARE @history_URL VARCHAR(55)
    DECLARE @history_access VARCHAR(55)

    SET @history_URL = (SELECT URLAddress FROM inserted)
    SET @history_access = (SELECT LastAccess FROM inserted)

    IF EXISTS (SELECT 1 FROM dbo.History AS H WHERE H.ID = @id)
        BEGIN
            UPDATE dbo.History
            SET LastAccess = @history_access
            WHERE ID = @id
        END
    ELSE
        -- dodajemy coś czego wcześniej nie było w dbo.History, usuwamy dodany do dbo.History rekord z dbo.Cache
        BEGIN
            SET IDENTITY_INSERT dbo.History ON
            INSERT INTO dbo.History (ID, URLAddress, LastAccess)
            VALUES (@id, @history_URL, @history_access)
            SET IDENTITY_INSERT dbo.History OFF 
        END
    
    -- wykasowanie zużytego rekordu z dbo.Cache
    DELETE FROM dbo.Cache
    WHERE ID = @id

END
GO

CREATE TRIGGER tr_access_website ON dbo.Cache
INSTEAD OF INSERT
AS
BEGIN
    -- SELECT * FROM inserted
    -- zmienna przechowująca adres strony, którą próbójemy dodać
    -- dodajemy pojedynczy wiersz, bierzemy z niego aktualny adres i datę dodania
    DECLARE @current_URL VARCHAR(55)
    DECLARE @current_date VARCHAR(55)
    
    SET @current_URL = (SELECT URLAddress FROM inserted)
    SET @current_date = (SELECT LastAccess FROM inserted)
    
    -- dodawana strona jest w Cache, zmieniamy tylko datę dostępu
    IF EXISTS (SELECT 1 FROM dbo.Cache AS C WHERE C.URLAddress = @current_URL)
        BEGIN
            UPDATE dbo.Cache
            SET LastAccess = @current_date
            WHERE URLAddress = @current_URL
        END
    ELSE
        BEGIN
            -- jak jest miejsce w cache to dodajemy nową witrynę
            IF (SELECT COUNT(*) FROM dbo.Cache) < (SELECT Value FROM dbo.Parameters WHERE Name = 'max_cache')
                BEGIN
                    INSERT INTO dbo.Cache
                    VALUES (@current_URL, @current_date)
                END
            ELSE
                -- nie ma miejsca w cache, znajdujemy najstarszy LastAccess w Cache
                BEGIN
                    -- pobieramy ID tego dostępu który był najdawniej
                    DECLARE @oldest_access_id INT
                    SET @oldest_access_id = (SELECT TOP 1 ID
                                            FROM dbo.Cache
                                            ORDER BY LastAccess ASC)
                    


                    -- pobieramy URL
                    DECLARE @oldest_URL VARCHAR(55)
                    SET @oldest_URL = (SELECT URLAddress
                                        FROM dbo.Cache AS C WHERE C.ID = @oldest_access_id)


                    -- pobieramy LatestAccess
                    DECLARE @oldest_access VARCHAR(55)
                    SET @oldest_access = (SELECT LastAccess
                                        FROM dbo.Cache AS C WHERE C.ID = @oldest_access_id)
                    

                    SET IDENTITY_INSERT dbo.History ON
                    INSERT INTO dbo.History (ID, URLAddress, LastAccess)
                    VALUES (@oldest_access_id, @oldest_URL, @oldest_access)
                    SET IDENTITY_INSERT dbo.History OFF

                    -- na końcu dodajemy rekord do dbo.Cache
                    INSERT INTO dbo.Cache
                    VALUES (@current_URL, @current_date)
                END
        END
END
GO

-- INSERT INTO dbo.Cache
-- VALUES ('https://stackoverflow.com/', GETDATE())

-- INSERT INTO dbo.Cache
-- VALUES ('https://stackoverflow1.com/', GETDATE())

-- INSERT INTO dbo.Cache
-- VALUES ('https://stackoverflow2.com/', GETDATE())

SELECT * FROM dbo.History

SELECT * FROM dbo.Cache

GO