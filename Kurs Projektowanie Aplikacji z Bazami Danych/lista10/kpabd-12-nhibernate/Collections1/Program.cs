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
	Fotka varchar(80)
)
go

SELECT * FROM Fotki;
SELECT * FROM Osoba;
GO

*/

using System.Collections.Generic;
using NHibernate;
using NHibernate.Cfg;

namespace Collections1
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
                ISet<string> lista = new HashSet<string>();
                lista.Add( "A.jpg" );
                lista.Add( "B.jpg" );
                lista.Add( "C.jpg" );
                var o = new Osoba { Imie = "Jan", Nazwisko = "Kowalski", Fotki = lista };
                s.Save( o );
                s.Flush();
            }
        }
    }
}
