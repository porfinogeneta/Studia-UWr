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
	ID int primary key identity,
	ID_Osoba int,
	Fotka varchar(80)
)
go

SELECT * FROM Fotki;
SELECT * FROM Osoba;
GO
*/


using NHibernate;
using NHibernate.Cfg;
using System.Collections.Generic;

namespace Collections2
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static void Main( string[] args )
        {
            using ( var s = OpenSession() )
            {
                IList<string> lista = new List<string>();
                lista.Add( "A.jpg" );
                lista.Add( "B.jpg" );
                lista.Add( "B.jpg" );
                lista.Add( "B.jpg" );
                lista.Add( "C.jpg" );
                var o = new Osoba { Imie = "Jan", Nazwisko = "Kowalski", Fotki = lista };
                s.Save( o );
                s.Flush();
            }
        }
    }
}
