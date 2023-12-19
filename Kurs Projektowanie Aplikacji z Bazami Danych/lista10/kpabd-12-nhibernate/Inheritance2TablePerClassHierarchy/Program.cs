/*
drop table if exists Osoba;
go

create table Osoba
(
	ID int primary key identity,
	Imie varchar(30),
	Nazwisko varchar(50),
	Pensja int,
	Stanowisko varchar(20),
	Licencja varchar(30),
	Osoba_Type varchar(30)
)
go 

SELECT * FROM Osoba;
GO
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NHibernate.Cfg;
using NHibernate;

namespace Inheritance2TablePerClassHierarchy
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
