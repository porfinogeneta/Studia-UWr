S1:
drop table if exists liczby1;
drop table if exists liczby2;
create table liczby1 ( liczba int )
create table liczby2 ( liczba int )
go

-- S1:
-- SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- begin tran
-- insert liczby1 values ( 1 )
-- S2:
-- SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- begin tran
-- insert liczby2 values ( 1 )
-- GO
-- S1:
-- update liczby2 set liczba=10
-- S2:
-- update liczby1 set liczba=10

-- i tutaj pojawia się zakleszczenie

-- na READ UNCOMMITTED też działa, jest jakiś problem z tym zadaniem