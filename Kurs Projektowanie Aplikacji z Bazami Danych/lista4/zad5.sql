-- SELECT name AS 'Database name', is_recursive_triggers_on AS 'Recursive Triggers Enabled'
-- FROM sys.databases

-- ALTER TABLE żeby uruchomić rekurencyjne triggery

-- 1 --
drop table if exists liczby
drop table if exists noweliczby
go
create table liczby( liczba int )
create table noweliczby( liczba int check (liczba<=20) )
go


drop trigger if exists tr_insert_liczby
drop trigger if exists tr_insert_noweliczby
go

-- to się uruchomi zamiast insert do liczb
create trigger tr_insert_liczby on liczby instead of insert
as
begin
  if ( @@nestlevel>3 ) return -- głębokość rekursji to maksymalnie 3
  print 'Wstawiono wiersz do liczby; poziom '+cast( @@nestlevel as varchar )
  insert liczby select * from inserted -- to nie uruchomi tego triggera drugi, blokada sql
  print 'Liczby; krok 2'
  insert noweliczby select * from inserted
  print 'Liczby; koniec'
end
go

-- uruchomi się zamiast insert do noweliczby
create trigger tr_insert_noweliczby on noweliczby instead of insert
as
begin
  if ( @@nestlevel>3 ) return -- głębokość rekursji to maksymalnie 2
  print 'Wstawiono wiersz do noweliczby; poziom '+cast( @@nestlevel as varchar )
  insert noweliczby select * from inserted -- to nie uruchomi tego triggera drugi, blokada sql
  print 'Noweliczby; krok 2'
  insert liczby select * from inserted
  print 'Noweliczby; koniec'
end
go

-- start

-- sp_configure 'nested triggers', 1
-- go
-- reconfigure
-- go

-- delete from liczby
-- delete from noweliczby
insert liczby values(5)
select * from liczby
select * from noweliczby

-- na początku uruchamia się trigger liczby, który uruchamia tylko trigger noweliczby,
-- który uruchamia trigger liczby, potem mamy koniec na 3 poziomie rekursji i wracamy w górę po drzewie wywołań

-- @@nestlevel zwraca nam numer wywołania danego triggera, zabezpiecza nas przed nieskończoną rekursją
-- nieparzyste wywołania ma trigger liczby a parzyste noweliczby