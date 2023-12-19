/*
--EXEC sp_fkeys 'produkt'
--EXEC sp_fkeys @pktable_name = 'produkt', @pktable_owner = 'dbo'

DROP TABLE IF EXISTS koszyk
GO
DROP TABLE IF EXISTS produkt
GO
DROP TABLE IF EXISTS atrybuty
GO
create table koszyk ( id int primary key identity, klient varchar(50) );
GO
create table produkt ( id int primary key identity, nazwa varchar(50), cena float, koszyk_id int references koszyk( id ) );
GO
create table atrybut ( id int primary key identity, wartosc varchar(50), produkt_id int references produkt( id ) );
GO

select * from koszyk;
select * from produkt;
select * from atrybuty;
GO

delete koszyk;
delete produkt;
delete atrybuty;
GO
*/
using System;
using System.Linq;
using NHibernate;
using NHibernate.Cfg;

namespace FetchingStrategies
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }
        static void Main( string[] args )
        {
            {
                Console.WriteLine("--------------------- Przygotowanie danych ---------------------");
                Koszyk k1 = new Koszyk { Klient = "Jan Kowalski" };
                for (int i = 0; i < 5; i++)
                {
                    Produkt p = new Produkt { Nazwa = "Banan" + i, Cena = i + 100, Koszyk = k1 };
                    k1.Produkty.Add(p);
                    for (int j = 0; j < 5; ++j)
                    {
                        Atrybut a = new Atrybut { Wartosc = "A" + j, Produkt = p };
                        p.Atrybuty.Add(a);
                    }
                }
                Koszyk k2 = new Koszyk { Klient = "John Maliniak" };
                for (int i = 0; i < 4; i++)
                {
                    Produkt p = new Produkt { Nazwa = "Serek" + i, Cena = i * 2 + 40, Koszyk = k1 };
                    k2.Produkty.Add(p);
                    for (int j = 0; j < 4; ++j)
                    {
                        Atrybut a = new Atrybut { Wartosc = "A" + j, Produkt = p };
                        p.Atrybuty.Add(a);
                    }
                }

                ISession s = OpenSession();

                ITransaction tx0 = s.BeginTransaction();
                s.Delete("from Koszyk");
                tx0.Commit();

                ITransaction tx1 = s.BeginTransaction();
                s.Save(k1);
                s.Save(k2);
                tx1.Commit();
                s.Close();
            }

            Console.WriteLine( "===================== Kolekcje =====================" );

            {
                Console.WriteLine( "--------------------- Fetch immediately ---------------------" );
                Console.WriteLine( "-- Ustawienia: fetch='select' lazy='false' (Koszyk, Produkt)" );

                Console.WriteLine( "--------------------- Fetch lazy ---------------------" );
                Console.WriteLine( "-- Ustawienia: fetch='*' lazy='true' (Koszyk, Produkt)" );

                // Poniższe nie działa
                Console.WriteLine( "--------------------- Fetch join ---------------------" );
                Console.WriteLine( "-- Ustawienia: fetch='join' lazy='false' (Koszyk, Produkt)" );

                Console.WriteLine( "--------------------- Fetch batch ---------------------" );
                Console.WriteLine( "-- Ustawienia: fetch='select' lazy='true' batch-size='4' (Produkt)" );

                var s = OpenSession();

                // Poniższe dla immediately, lazy, join
                //var result = s.CreateQuery("from Koszyk").List<Koszyk>();

                // Poniższe dla batch (raz włączamy batch, a drugi raz wyłączamy)
                var result2 = s.CreateQuery( "from Produkt" ).List<Produkt>();
                Console.WriteLine( result2.First().Atrybuty.Count );

                s.Close();
            }

            Console.WriteLine( "===================== Pojedyncze obiekty =====================" );

            {

                //Console.WriteLine( "--------------------- Fetch immediately ---------------------" );
                //Console.WriteLine( "-- Ustawienia: fetch='select' lazy='false' (Atrybut)" );

                //// Nie działa
                //Console.WriteLine( "--------------------- Fetch lazy ---------------------" );
                //Console.WriteLine( "-- Ustawienia: fetch='select' lazy='proxy' (Atrybut)" );

                //// Nie działa - i to jest problem...
                //Console.WriteLine( "--------------------- Fetch join ---------------------" );
                //Console.WriteLine( "-- Ustawienia: fetch='join' (Atrybut)" );

                //var s = OpenSession();

                //var result = s.CreateQuery( "from Atrybut" ).List<Atrybut>();

                //s.Close();
            }

            Console.ReadLine();

        }
    }
}
