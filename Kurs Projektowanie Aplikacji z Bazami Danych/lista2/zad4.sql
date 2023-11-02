DROP PROCEDURE IF EXISTS reader_rec;
GO

DROP TYPE IF EXISTS CZYTELNIK_IDsTABLETYPE;
GO

CREATE TYPE CZYTELNIK_IDsTABLETYPE AS TABLE(
    ID INT
)
GO


CREATE PROCEDURE reader_rec @czytelnik_id CZYTELNIK_IDsTABLETYPE READONLY
AS
BEGIN
    SELECT CZ.ID AS reader_id, SUM(WYP.Liczba_Dni) AS sum_days
    FROM @czytelnik_id AS CZ
    INNER JOIN dbo.Wypozyczenie AS WYP
    ON WYP.Czytelnik_ID = CZ.ID
    GROUP BY CZ.ID;
END;
GO

-- decleare table
DECLARE @czytelnik_ids CZYTELNIK_IDsTABLETYPE

-- populate table with data
INSERT INTO @czytelnik_ids (ID)
SELECT CZ.Czytelnik_ID
FROM dbo.Czytelnik AS CZ;


EXEC reader_rec @czytelnik_id = @czytelnik_ids;
