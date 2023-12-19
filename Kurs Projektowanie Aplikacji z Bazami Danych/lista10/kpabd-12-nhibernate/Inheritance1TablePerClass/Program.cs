/*

drop table if exists Pracownik;
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
	ID int primary key identity,
	Imie varchar(30),
	Nazwisko varchar(50),
	Pensja int,
	Stanowisko varchar(20)
)
go

SELECT * FROM Pracownik;
SELECT * FROM Osoba;
GO
*/

using NHibernate;
using NHibernate.Cfg;

namespace Inheritance1TablePerClass
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static void Main( string[] args )
        {
            var p = new Pracownik { Imie = "Jan", Nazwisko = "Kowalski", Pensja = 1200, Stanowisko = "Palacz" };
            var o = new Osoba { Imie = "Edward", Nazwisko = "Malinowski" };

            using ( var s = OpenSession() )
            {
                s.Save( p );
                s.Save( o );
                s.Close();
            }
        }
    }
}
