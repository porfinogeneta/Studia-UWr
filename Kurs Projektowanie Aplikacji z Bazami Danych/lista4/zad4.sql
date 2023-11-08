DROP TRIGGER IF EXISTS tr_check_for_5 
GO

CREATE TRIGGER tr_check_for_5 ON dbo.Egzemplarz INSTEAD OF INSERT
AS
BEGIN
    -- liczymy egzemplarze w inserted
    IF NOT EXISTS (
        SELECT E.Ksiazka_ID,
        COUNT(E.Ksiazka_ID) AS Amount
        FROM dbo.Egzemplarz AS E
        GROUP BY E.Ksiazka_ID
        HAVING COUNT(E.Ksiazka_ID) >= 5)
        BEGIN
            INSERT INTO dbo.Egzemplarz (Sygnatura, Ksiazka_ID)
            SELECT Sygnatura, Ksiazka_ID
            FROM INSERTED
        END
    ELSE
        BEGIN
            RAISERROR('This book has more than 5 specimen!', 16, 1)
            ROLLBACK TRANSACTION
            RETURN
        END
END
GO

INSERT INTO dbo.Egzemplarz(Sygnatura, Ksiazka_ID)
VALUES ('S0019', 1)

