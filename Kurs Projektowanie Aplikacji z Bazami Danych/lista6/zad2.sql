-- DBCC FREEPROCCACHE -- wyczyszczenie bufora SET SHOWPLAN_ASET SHOWPLAN_ALL

/*
▪ Plany wykonania są przechowywane w buforze
▪ Przed wykonaniem zapytania:
     Jeśli plan już jest, zostaje wykorzystany
     Jeśli go nie ma, zostaje utworzony i zachowany

 W planie wykonania mamy
    ▪ Elementy języka (zielone)
    ▪ Operatory fizyczne/logiczne (niebieskie)
    ▪ Operacje związane z kursorem (żółte)
 Plan wykonania jest w postaci drzewa
    ▪ Drzewa, które powstaje po sparsowaniu zapytania
 Po najechaniu na węzeł dostajemy sporo
dodatkowych szczegółów
*/


-- krótki opis dla planów
/*
EstimateIO - szacowany koszt dla danego operatora
EstimateRows - szacowana liczba wierszy zwróconych przez dany operator
StmtText - opis danej operacji
EstimateExecutions - szacowana liczba wywołań danego operatora 
więcej: https://sqlserverrider.com/2013/06/14/sql-server-set-showplan_all-set-statement/
https://learn.microsoft.com/en-us/sql/t-sql/statements/set-showplan-text-transact-sql?view=sql-server-ver16
https://learn.microsoft.com/en-us/sql/t-sql/statements/set-statistics-profile-transact-sql?view=sql-server-ver16
*/

-- przed wykonaniem
-- GO
-- SET SHOWPLAN_ALL ON
-- GO
-- GO  
-- SET SHOWPLAN_TEXT ON;  -- zwraca po prostu String'a z naszym query
-- GO
-- po wykonaniu
-- GO
-- SET STATISTICS PROFILE ON;
-- GO
SELECT DISTINCT c.PESEL, c.Nazwisko
FROM Egzemplarz e
JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
JOIN Wypozyczenie w ON e.Egzemplarz_ID = w.Egzemplarz_ID
JOIN Czytelnik c ON c.Czytelnik_ID = w.Czytelnik_ID;
-- GO
-- SET STATISTICS PROFILE OFF;
-- GO
-- GO
-- SET SHOWPLAN_ALL OFF
-- GO
-- GO  
-- SET SHOWPLAN_TEXT OFF;  
-- GO

-- GO
-- SET SHOWPLAN_ALL ON
-- GO
-- GO
-- SET STATISTICS PROFILE ON;
-- GO
SELECT c.PESEL, c.Nazwisko
FROM Czytelnik c WHERE c.Czytelnik_ID IN
(SELECT w.Czytelnik_ID FROM Wypozyczenie w
JOIN Egzemplarz e ON e.Egzemplarz_ID=w.Egzemplarz_ID
JOIN Ksiazka k ON e.Ksiazka_ID=k.Ksiazka_ID)
-- GO
-- SET STATISTICS PROFILE OFF;
-- GO
-- GO
-- SET SHOWPLAN_ALL OFF
-- GO

/*
Porównując oba plany można zauważyć, że instrukcje w drugim planie
- jest ich mniej, przez co zajmują mniej czasu procesora
- nie ma instrukcji, którą musielibyśmy wykonać więcej niż 10 razy
- instrukcje operują na mniejszej liczbie wierszy i mniej tych wierszy produkują
*/

-- pobierz czytelników, którzy wypożyczeli jakiś egzamplarz ksiązki, która jest w egzemplarzach
-- ANALIZA PLANU
-- zużywamy mało poleceń i przez to zajmuje nam to całkiem niewiele czasu procesora
-- polecenia zwracają niewielką liczbę wierszy - max 3

-- GO
-- SET SHOWPLAN_ALL ON
-- GO

-- GO
-- SET STATISTICS PROFILE ON;
-- GO
SELECT c.PESEL, c.Nazwisko
FROM Czytelnik c WHERE c.Czytelnik_ID IN
(SELECT w.Czytelnik_ID FROM Wypozyczenie w
    WHERE w.Egzemplarz_ID IN (
        SELECT e.Egzemplarz_ID
        FROM Egzemplarz e
        JOIN Ksiazka k ON e.Ksiazka_ID=k.Ksiazka_ID
    )
)
-- GO
-- SET SHOWPLAN_ALL OFF
-- GO
-- GO
-- SET STATISTICS PROFILE OFF;
-- GO
-- 
