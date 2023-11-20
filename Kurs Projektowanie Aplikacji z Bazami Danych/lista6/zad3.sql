/*
 Indeks to struktura danych mająca na celu
    przespieszenie pobierania danych
    ▪ Indeksy są przechowywane w strukturze B-drzewa
 Jest związana z tabelą lub widokiem oraz jej/jego
    wybranymi kolumnami
    ▪ Indeksować można prawie wszystko oprócz głównie
    LOB (np. images, text, varchar(max))
 Dobór odpowiednich indeksów jest balansem
    pomiędzy
    ▪ Szybkością pobierania danych
    ▪ Kosztem związanym z jego utrzymaniem (CRUD)
*/

/*
 Indeks zgrupowany (clustered index)
    ▪ Może być tylko jeden w tabeli
    ▪ Wyznacza on porządek danych w samej tabeli
    ▪ Zawiera faktyczne wartości rekordów

 Indeks niezgrupowany (nonclustered index)
    ▪ Może być ich wiele w tabeli
    ▪ Nie zawiera danych tylko referencje do nich
    ▪ Na poziomie liści można dołączyć tzw. included
    columns, które nie są indeksowane

 Covering Index
 - rodzaj indeksu, który zachowuje już raz pobrane dane
 - CLUSTERED INDEX jest w rzeczywistości COVERING INDEX, bo zazwyczaj to jest jakiś klucz, który pobieramy kilkukrotnie
 - zawiera wszystkie informacje do obliczenie kwerendy
*/
-- INDEXY DLA KSIAZKI_IDX
DROP INDEX IF EXISTS IX_Ksiazka_PK on dbo.Ksiazka_idx
go
CREATE UNIQUE clustered INDEX IX_Ksiazka_PK ON dbo.Ksiazka_idx (Ksiazka_ID);
go
-- NONCLUSTERED INDEX
DROP INDEX IF EXISTS IX_Ksiazka_ISBN on dbo.Ksiazka_idx
go
CREATE NONCLUSTERED INDEX IX_Ksiazka_ISBN ON dbo.Ksiazka_idx (ISBN);
go
-- ROBIMY GRUPOWY INDEX
DROP INDEX IF EXISTS IX_Ksiazka_GROUP on dbo.Ksiazka_idx
go
-- CREATE NONCLUSTERED INDEX IX_Ksiazka_GROUP ON dbo.Ksiazka_idx (ISBN, Cena, Tytul, Autor);
-- go
-- teraz COVERING INDEX, czyli dodajemy często używane dane do NONCLUSTERED index
-- podłączamy je do INDEXU ISBN, bo jak go pobierzemy to chcemy mieć od razu pobrane Ksiazka_ID, Cena, Tytul, Autor
DROP INDEX IF EXISTS IX_Ksiazka_COVER on dbo.Ksiazka_idx
go
/*
By including frequently queried columns in nonclustered indexes, 
we can dramatically improve query performance by reducing I/O costs.
Since the data pages for an nonclustered index are frequently readily
available in memory, covering indexes are the usually the ultimate in query resolution.
https://learn.microsoft.com/en-us/answers/questions/94659/can-we-create-cover-index-during-cluster-index-cre
*/
-- CREATE NONCLUSTERED INDEX IX_Ksiazka_COVER ON dbo.Ksiazka_idx(ISBN) INCLUDE (Ksiazka_ID, Cena, Tytul, Autor);
-- go

-- INDEKSY DLA EGZEMPLARZ_IDX
DROP INDEX IF EXISTS IX_Egzemplarz on dbo.Egzemplarz_idx
go
DROP INDEX IF EXISTS IX_Egzemplarz_Ksiazka_ID on dbo.Egzemplarz_idx
go
CREATE clustered INDEX IX_Egzemplarz ON dbo.Egzemplarz_idx (Egzemplarz_ID);
go
CREATE NONCLUSTERED INDEX IX_Egzemplarz_Ksiazka_ID ON dbo.Egzemplarz_idx (Ksiazka_ID);
go

GO
SET SHOWPLAN_ALL ON
GO
SELECT DISTINCT k.Ksiazka_ID, k.ISBN, k.Cena, k.Tytul, k.Autor FROM dbo.Ksiazka_idx k
JOIN dbo.Egzemplarz_idx e ON e.Ksiazka_ID = k.Ksiazka_ID
WHERE k.ISBN <> '978-83-246-2188-0'
GO
SET SHOWPLAN_ALL OFF
GO
-- dla COVERING INDEX mamy tylko nieco inne operacje, dla tej ilości danych mamy te same czasy
-- Clustered Index Scan - bez covering
-- Index Seek z covering