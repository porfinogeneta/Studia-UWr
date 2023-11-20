GO
SET STATISTICS TIME ON
GO
SELECT DISTINCT c.PESEL, c.Nazwisko
FROM Egzemplarz e
JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
JOIN Wypozyczenie w ON e.Egzemplarz_ID = w.Egzemplarz_ID
JOIN Czytelnik c ON c.Czytelnik_ID = w.Czytelnik_ID;
go
SET STATISTICS TIME OFF
GO

/*
powklejać kolejne   QUERY
BADAMY 1, 2 i 3 QUERY
czasem się udaje porównać czas, czasem nie
SQL Server Execution Times:
   CPU time = 4 ms,  elapsed time = 3 ms.

==========================================
SQL Server Execution Times:
   CPU time = 0 ms,  elapsed time = 0 ms.
===========================================
SQL Server Execution Times:
   CPU time = 1 ms,  elapsed time = 0 ms.


*/