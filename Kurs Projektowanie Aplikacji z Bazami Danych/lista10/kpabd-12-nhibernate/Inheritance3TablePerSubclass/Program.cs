/*
drop table if exists Pracownik;
go
drop table if exists Klient;
go
drop table if exists Osoba;
go
create table Osoba
(
	ID int primary key identity,
	Imie varchar(30),
	Nazwisko varchar(50)
)
go

create table Pracownik
(
	ID int primary key references Osoba( ID ),
	Pensja int,
	Stanowisko varchar(20)
)
go
create table Klient
(
	ID int primary key references Osoba( ID ),
	Licencja varchar(30)
)
go

SELECT * FROM Pracownik;
SELECT * FROM Klient;
SELECT * FROM Osoba;
GO
*/

using NHibernate.Cfg;
using NHibernate;

namespace Inheritance3TablePerSubclass
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static void Main( string[] args )
        {
            var p = new Pracownik { Imie = "Jan", Nazwisko = "Kowalski", Pensja = 1200, Stanowisko = "Palacz" /* null */ };
            var o = new Osoba { Imie = "Edward", Nazwisko = "Malinowski" };
            var k = new Klient { Imie = "Franciszek", Nazwisko = "Wydojony", Licencja = "002434" };

            using ( var s = OpenSession() )
            {
                s.Save( p );
                s.Save( k );
                s.Save( o );
                s.Close();
            }
        }
    }
}
