/*
drop table if exists KsiazkaKategoria;
go
drop table if exists Ksiazka;
go
drop table if exists Kategoria;
go
create table Ksiazka
(
	ID int primary key identity,
	Tytul varchar(34),
	Autor varchar(20)
)
go

create table Kategoria
(
	ID int primary key identity,
	Nazwa varchar(20)
)
go

create table KsiazkaKategoria
(
	KsiazkaID int,
	KategoriaID int,
)
go

SELECT * FROM Ksiazka;
SELECT * FROM Kategoria;
SELECT * FROM KsiazkaKategoria;
GO
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NHibernate;
using NHibernate.Cfg;

namespace Associations2ManyToMany
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static void Main(string[] args)
        {
            var ks1 = new Ksiazka { Tytul = "T1", Autor = "A1" };
            var ks2 = new Ksiazka { Tytul = "T2", Autor = "A2" };
            var ks3 = new Ksiazka { Tytul = "T3", Autor = "A3" };

            var kat1 = new Kategoria { Nazwa = "K1" };
            var kat2 = new Kategoria { Nazwa = "K2" };

            // 1. Nie działa
            //ks1.Kategorie.Add(kat1);
            //ks2.Kategorie.Add(kat1);
            //ks2.Kategorie.Add(kat2);
            //ks3.Kategorie.Add(kat2);
            // 2. Działa
            kat1.Ksiazki.Add(ks1);
            kat1.Ksiazki.Add(ks2);
            kat2.Ksiazki.Add(ks2);
            kat2.Ksiazki.Add(ks3);


            using (var s = OpenSession())
            {
                //s.SaveOrUpdate(ks1);
                //s.SaveOrUpdate(ks2);
                //s.SaveOrUpdate(ks3);
                s.SaveOrUpdate(kat1);
                s.SaveOrUpdate(kat2);
                s.Flush();
            }
        }
    }
}
