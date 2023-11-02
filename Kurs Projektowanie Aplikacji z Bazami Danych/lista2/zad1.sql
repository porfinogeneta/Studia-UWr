drop function if EXISTS reader_specimen
go

create FUNCTION reader_specimen(@days_number INT) RETURNS @table TABLE(PESEL VARCHAR(15), specimens_number INT)
BEGIN

    INSERT INTO @table (PESEL, specimens_number)
    SELECT CZ.PESEL, COUNT(WYP.Egzemplarz_ID)
    FROM dbo.Czytelnik AS CZ
    INNER JOIN dbo.Wypozyczenie AS WYP
    ON CZ.Czytelnik_ID = WYP.Czytelnik_ID
    WHERE WYP.Liczba_Dni >= @days_number
    GROUP BY CZ.PESEL

    RETURN
END
go

SELECT * FROM reader_specimen(20)