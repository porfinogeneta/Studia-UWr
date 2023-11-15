-- rodzaje blokad
drop table if exists liczby;
go
create table liczby ( liczba int );
go
insert liczby values ( 10 );
go

-- niski poziom blokady, zwolniony zaraz po odczycie wiersza
-- wysoki poziom blokady - zwalnia po zakończeniu transakcji

-- S - Shared uniemożliwia modyfikacje przez inne transakcje
-- X - Exclusive - Dają wyłączność dostępu do zasobu; Niezbędne dla operacji INSERT, UPDATE, DELETE
-- U - Update - chęć modyfikacji danych

-- tryby blokad
/*
    ▪ IS – transakcja zamierza czytać część zasobów przez
        nałożenie na nie blokady S, elementy niższego poziomu
    ▪ IX – transakcja zamierza modyfikować część zasobów
        poprzez nałożenie na nie blokady X
    ▪ SIX – transakcja zamierza czytać wszystkie wiersze i niektóre
        z nich modyfikować (poprzez nakładanie odpowiednich
        blokad)
*/

-- 1 --
-- izolacja transakcji chroni nas przed DIRTY READ, NON-REPEATABLE
-- zakładamy tutaj Shared Lock'a na wszystkie elementy odczytywane w transakcji
-- sp_lock wyświetli nam tabelkę blokad
--
set transaction isolation level repeatable read
-- odczytuj dane, które się nie powtarzają, załóż lock'a na rzędy, które ulegają update'owi
begin transaction

-- w drugim połączeniu robimy update: update liczby set liczba=4
-- oglądamy blokady: sp_lock

EXEC sp_lock -- blokady położone są na wszystko w tabelce

select * from liczby
-- blokada jest nałożona na update'towany wiersz
EXEC sp_lock 

-- ponownie w drugim połączeniu robimy update: update liczby set liczba=4
-- oglądamy blokady: sp_lock


-- na początku blokada całej naszej tabelki IS, co oznacza że jest zmieniane coś wewnątrz tabelki (widać w pierwszym sp_lock),
-- ostatecznie blokada ustawiona na rząd w tabelce

commit

-- 2 --
-- to nas chroni przed wszystkimi anomaliami, poprzez wprowadzenie lock'a na wszystkich zakresach wartości
-- które są używane w całej transakcji
set transaction isolation level serializable;
-- -- założ lock'a na całą tabelkę, żeby nie można było insertować
insert liczby values ( 10 );

begin transaction

-- w drugim połączeniu robimy insert: insert liczby values(151)
-- oglądamy blokady: sp_lock
EXEC sp_lock
select * from liczby
EXEC sp_lock
-- ponownie w drugim połączeniu robimy insert: insert liczby values(151)
-- oglądamy blokady: sp_lock

-- tutaj nasz lock jest nałożony na całą tabelkę, co uniemożliwia nam
-- zrobienie tymczasowego inserta, widać to w sp_lock, gdzie zablokowana jest tabelka

commit


-- Server Repeatable Read Isolation Level
-- As mentioned above, the Repeatable Read SQL Server isolation level prevents dirty reads and not-repeatable reads.
-- It is achieved by placing shared locks on all data that is read by each statement in a transaction and all the locks
-- are held until the transaction completes. As a result other transactions are unable to modify the data that has been 
-- read by the current transaction. However, it does not prevent other transactions from inserting new rows into the tables
-- which have been selected in the current transaction, moreover these new rows can match the select conditions in the
-- current transaction statements. So, if these statements are issued in the current transaction more than once and the
-- mentioned new rows are inserted between executions of these statements, phantom reads occur. 

-- Server Serializable Isolation Level
-- The Serializable SQL Server isolation level protects from all three consistency anomalies and this is
-- done by placing range locks in the range of key values that match search conditions for all statements
-- in the transaction. These locks are held until the transaction ends. This ensures that not only dirty reads
--  and not-repeatable reads are prevented, but also phantom reads are excluded. Serializable is the strictest
-- isolation level, but concurrency is lower than in other transaction isolation levels. 