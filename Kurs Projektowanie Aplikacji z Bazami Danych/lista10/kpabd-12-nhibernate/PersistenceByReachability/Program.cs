/*
DROP TABLE IF EXISTS koszyk
GO
DROP TABLE IF EXISTS produkt
GO
DROP TABLE IF EXISTS atrybuty
GO
create table koszyk ( id int primary key identity, klient varchar(50) );
GO
create table produkt ( id int primary key identity, nazwa varchar(50), cena float, koszyk_id int );
GO
create table atrybuty ( koszyk_id int, atrybut varchar(255) );
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
using System.Linq;
using NHibernate;
using NHibernate.Cfg;

namespace PersistenceByReachability
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }
        static void Main(string[] args)
        {
            Produkt p1 = new Produkt { Nazwa = "Banany", Cena = 3.0 };
            Produkt p2 = new Produkt { Nazwa = "Czekolada", Cena = 4.0 };

            Koszyk k = new Koszyk { Klient = "Jan Kowalski" };
            k.Produkty.Add(p1);
            k.Produkty.Add(p2);

            k.Atrybuty.Add("data powstania");
            k.Atrybuty.Add("data realizacji");

            // W pliku mapującym upewniamy się, że w obu miejscach jest save-update
            var session1 = OpenSession();
            var tx1 = session1.BeginTransaction();
            session1.Save(k);
            tx1.Commit();

            
            // Poniższe wykonujemy dwa razy: raz bez zmian, za drugim razem dodajemy delete-orphan
            var tx2 = session1.BeginTransaction();
            Produkt p = k.Produkty.First();
            string s = k.Atrybuty.First();
            k.Produkty.Remove(p);
            k.Atrybuty.Remove(s);
            //session1.delete(p); // nie chcemy musieć to wywołać
            tx2.Commit();
            

            // Poniższe wykonujemy dwa razy: raz bez zmian, za drugim razem dodajemy delete
            var tx3 = session1.BeginTransaction();
            session1.Delete(k);
            tx3.Commit();

            session1.Close();
        }
    }
}
