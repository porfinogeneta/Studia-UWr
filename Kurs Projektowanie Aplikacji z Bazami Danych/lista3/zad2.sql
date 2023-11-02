-- wyłączenie komunikatu row-affected
set nocount on

drop table if exists liczby
go
create table liczby( nr int primary key, liczba int )
go
-- wypełnienie tabelki liczbami [1;60]
declare @a int
set @a=1
while ( @a<=60)
begin
  insert liczby values ( @a, @a )
  set @a=@a+1
end
go

declare @x int
set @x=10

-- Do wykonania 3 razy (każde z osobna, analizujemy wyniki: results i messages)
-- declare c cursor for select liczba from liczby where liczba<=@x
-- declare c cursor static for select liczba from liczby where liczba<=@x
declare c cursor keyset for select liczba from liczby where liczba<=@x

set @x=20

open c

declare @aux int, @licznik int
set @licznik=2

print 'Kolejne liczby z kursora:'
-- wrzucamy kolejne liczby z tabelki do zmiennej @aux
fetch next from c into @aux 
while ( @@fetch_status=0 ) -- dopóki się nie powtórzy wiersz
begin
  print @aux;
  print 'Liczba: '+cast(@aux as varchar)
  print 'Licznik: '+cast(@licznik as varchar)
  delete from liczby where liczba=@licznik -- wykasowanie co drugiej wartości z tabelki 'liczby'
  -- * dla statycznego kursora @aux będzie zawierało kolejne liczby, bo nie widzi on zmian w tabeli liczby, po otwarciu kursora
  -- * dla dynamicznego kursora @aux będzie zawierało tylko liczby nieparzyste, bo widzi on zmieniającą się tabelkę, z której usunięto wszetkie parzyste
  -- * dla keyset kursora wyliczony @aux będzie 1, ale przez skasowanie elementu z tabelki pętla zostanie przerwana (status -2)
  -- || na końcu otrzymamy tabelkę zaaktualizwaną, ale bez wiersza nr 2 i licznika 2, usuniętego w pierwszej iteracji, przerwanej pętli
  -- * Dlaczego przerwie pętlę - po skasowaniu elementu kursor spotyka się z sytuacją że nie może zlokalizować rzędu, który pierwotnie
  -- pobrał, bo został on bowiem usunięty, kursor pilnuje identyfikatorów dla rzędów które pierwotnie przeczytał
  fetch next from c into @aux -- pobranie kolejnego
  set @licznik=@licznik+2
end
print 'Status ostatniej instrukcji fetch: ' + cast(@@fetch_status as varchar)
-- dla keyset status to -2, czyli brak wiersza w kursorze kluczowym
-- jest to spowodowane tym, że przez skasowanie parzystej liczby już w pierwszej iteracji
-- pomieszałyby się klucze i pętla się od razu kończy
close c
deallocate c

select * from liczby where liczba<=10

-- rodzaje kursorów:
-- STATIC
-- * wszelkie zmiany dla danych, na których operuje kursor 
-- po jego otwarciu nie są dla niego widoczne, dostaje na wejściu snapshot z danymi
-- * szybsze bo nie muszą śledzić zmian w danych
-- * mogą tylko czytać dane, ale nie mogą ich zmieniać czy kasować

-- DYNAMIC
-- * wszeklkie zmiany danych są widoczne dla cursora
-- * wolniejsze od STATIC

-- KEYSET
-- * odczytują dane dynamicznie, ale zachowują stare unikalne identyfikatory
-- * odzytują dane z rzędu który akurat jest potrzebny
-- * nieco szybsze niż dynamiczne