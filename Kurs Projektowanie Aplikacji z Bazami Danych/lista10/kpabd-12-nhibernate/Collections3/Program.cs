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
	Nazwa varchar(40),
	Plik varchar(80)
)
go

SELECT * FROM Fotki;
SELECT * FROM Osoba;
GO

*/
using System;
using System.Collections.Generic;
using NHibernate;
using NHibernate.Cfg;

namespace Collections3
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
                IDictionary<string, string> lista = new Dictionary<string, string>();
                lista.Add( "A", "A.jpg" );
                lista.Add( "B", "B.jpg" );
                lista.Add( "C", "C.jpg" );
                
                var o = new Osoba { Imie = "Jan", Nazwisko = "Kowalski", Fotki = lista };
                s.Save( o );
                s.Flush();
            }

            using ( var s = OpenSession() )
            {
                var o = s.Get<Osoba>( 1 );
                foreach ( var i in o.Fotki )
                    Console.WriteLine( "{0} {1}", i.Key, i.Value );
            }
        }
    }
}
