/*
drop table if exists Fotki;
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

create table Fotki
(
	ID_Osoba int,
	Nazwa varchar(80),
	Sciezka varchar(80),
	RozmiarX int,
	RozmiarY int
)
go

SELECT * FROM Fotki;
SELECT * FROM Osoba;
GO

*/

using System.Collections.Generic;
using NHibernate;
using NHibernate.Cfg;

namespace Collections5
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
                ISet<Fotka> lista = new HashSet<Fotka>();
                lista.Add(new Fotka { Nazwa = "A", Sciezka = "A.jpg", RozmiarX = 100, RozmiarY = 120 });
                lista.Add(new Fotka { Nazwa = "B", Sciezka = "B.jpg", RozmiarX = 100, RozmiarY = 120 });
                lista.Add(new Fotka { Nazwa = "C", Sciezka = "C.jpg", RozmiarX = 100, RozmiarY = 120 });

                var o = new Osoba { Imie = "Jan", Nazwisko = "Kowalski", Fotki = lista };
                s.Save(o);
                s.Flush();
            }
        }
    }
}
