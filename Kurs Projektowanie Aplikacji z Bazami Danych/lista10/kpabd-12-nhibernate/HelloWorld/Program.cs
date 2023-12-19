/*
Przygotowanie bazy danych 

drop table if exists Osoba;
go
drop table if exists Jednostka;
go
create table Jednostka( ID int not null primary key identity, Nazwa varchar(20) );
go

SET IDENTITY_INSERT Jednostka ON
go

begin
  insert into Jednostka(ID, Nazwa) values( 1, 'Wrocław' );
  insert into Jednostka(ID, Nazwa) values( 2, 'Poznań' );
  insert into Jednostka(ID, Nazwa) values( 3, 'Kraków' );
  insert into Jednostka(ID, Nazwa) values( 4, 'Warszawa' );
end;
go

SET IDENTITY_INSERT Jednostka OFF
go

create table Osoba( ID int not null primary key identity, ID_Jednostka int references Jednostka(ID), Imie varchar(30), Nazwisko varchar(50), Pensja int)
go

SET IDENTITY_INSERT Osoba ON
go

begin
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 1, 1, 'Jan', 'Kowalski', 1000 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 2, 3, 'Ewa', 'Solska', 1200 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 3, 2, 'Bożydar', 'Nowak', 1500 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 4, 4, 'Adam', 'Adamski', 1700 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 5, 4, 'Zygmunt', 'Riposta', 1240 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 6, 2, 'Alicja', 'Gleba', 1600 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 7, 1, 'Tania', 'Borówka', 1560 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 8, 1, 'Natasza', 'Lizacka', 2500 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 9, 3, 'Stan', 'Taczkowski', 1900 );
end;
go

SET IDENTITY_INSERT Osoba ON
go

select * from Osoba o, Jednostka j where o.ID_Jednostka = j.ID; 
go
*/

using System;
using System.Collections.Generic;
using NHibernate;
using NHibernate.Cfg;

namespace HelloWorld
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }
        static void Main( string[] args )
        {
            Jednostka j1 = new Jednostka() { Nazwa = "Londyn" };
            using ( ISession s = OpenSession() )
            {
                s.Save(j1);
                s.Flush();
            }

            using (ISession s = OpenSession())
            {
                IQuery q = s.CreateQuery("from Jednostka as j order by j.Nazwa");
                IList<Jednostka> result = q.List<Jednostka>();
                Console.WriteLine("Znaleziono {0}", result.Count);
                foreach (var j in result)
                    Console.WriteLine(j.ToString());
            }
            Console.ReadLine();
        }
    }
}
