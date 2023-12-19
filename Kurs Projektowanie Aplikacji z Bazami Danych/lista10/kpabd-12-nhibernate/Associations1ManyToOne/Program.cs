/*
drop table if exists Osoba;
go
drop table if exists Stanowisko;
go

create table Stanowisko
(
	ID int primary key identity,
	Nazwa varchar(40),
	Pensja int
)
go

create table Osoba (
	ID int primary key identity,
	Imie varchar(30),
	Nazwisko varchar(50),
	StanowiskoID int references Stanowisko(ID)
)
go

SELECT * FROM Stanowisko;
SELECT * FROM Osoba;
GO

*/

using System.Linq;
using NHibernate;
using NHibernate.Cfg;
using NHibernate.Linq;

namespace Associations1ManyToOne
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static void Main(string[] args)
        {
            using (var s = OpenSession())
            {
                var s1 = new Stanowisko { Nazwa = "Palacz", Pensja = 1000 };
                var o1 = new Osoba { Imie = "Jan01", Nazwisko = "Kowalski01" };
                var o2 = new Osoba { Imie = "Jan02", Nazwisko = "Kowalski02" };

                // 1. Działa
                o1.Stanowisko = s1;
                o2.Stanowisko = s1;
                // 2. Nie działa
                //s1.Osoby.Add(o1);
                //s1.Osoby.Add(o2);

                s.SaveOrUpdate(o1);
                s.SaveOrUpdate(o2);
                s.Save(s1);
                s.Flush();
            }
            using (var s = OpenSession())
            {
                var result = from e in s.Query<Stanowisko>()
                             select e;
            }
        }
    }
}
