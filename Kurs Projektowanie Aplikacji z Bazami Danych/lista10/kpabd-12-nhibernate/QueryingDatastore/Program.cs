/*
drop table if exists produkt;
drop table if exists koszyk;
go

create table koszyk ( id int primary key identity, klient varchar(50) );
create table produkt ( id int primary key identity, nazwa varchar(50), cena float, koszyk_id int references koszyk( id ) );
go

select * from koszyk;
select * from produkt;
go
*/
using System;
using System.Collections.Generic;
using System.Linq;
using NHibernate;
using NHibernate.Cfg;
using NHibernate.Criterion;
using NHibernate.Linq;

namespace QueryingDatastore
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static void Main(string[] args)
        {
            Koszyk k1 = new Koszyk { Klient = "Jan Kowalski" };
            for (int i = 0; i < 50; i++)
            {
                Produkt p = new Produkt { Nazwa = "Banan" + i, Cena = i + 100, Koszyk = k1 };
                k1.Produkty.Add(p);
            }
            Koszyk k2 = new Koszyk { Klient = "John Maliniak" };
            for (int i = 0; i < 60; i++)
            {
                Produkt p = new Produkt { Nazwa = "Serek" + i, Cena = i * 2 + 40, Koszyk = k1 };
                k2.Produkty.Add(p);
            }

            ISession session1 = OpenSession();

            ITransaction tx0 = session1.BeginTransaction();
            session1.Delete("from Koszyk");
            tx0.Commit();



            ITransaction tx1 = session1.BeginTransaction();
            session1.Save(k1);
            session1.Save(k2);
            tx1.Commit();

            // Natywny SQL
            Console.WriteLine("------- NATYWNY SQL -------");
            ITransaction tx2 = session1.BeginTransaction();
            IList<Produkt> produkty = session1.CreateSQLQuery("select {p.*} from PRODUKT {p}")
                    .AddEntity("p", typeof(Produkt)).List<Produkt>();
            foreach (var p in produkty)
            {
                Console.WriteLine("{0} {1}", p.Nazwa, p.Cena);
            }
            tx2.Commit();

            // Stronicowanie 1
            Console.WriteLine("------- STRONICOWANIE 1 -------");
            ITransaction tx3 = session1.BeginTransaction();
            IList<Produkt> produkty2 = session1.CreateQuery("from Produkt p order by p.Nazwa asc")
                .SetFirstResult(30)
                .SetMaxResults(5)
                .List<Produkt>();
            foreach (var p in produkty2)
            {
                Console.WriteLine(p.Nazwa);
            }
            tx3.Commit();

            // Stronicowanie 2
            Console.WriteLine("------- STRONICOWANIE 2 -------");
            ITransaction tx4 = session1.BeginTransaction();
            IList<Produkt> produkty3 = session1.CreateCriteria(typeof(Produkt))
                    .AddOrder(Order.Asc("Nazwa"))
                    .SetFirstResult(20)
                    .SetMaxResults(4)
                    .List<Produkt>();
            foreach (var p in produkty3)
            {
                Console.WriteLine(p.Nazwa);
            }
            tx4.Commit();

            // Dowiązanie parametrów pozycyjnych
            Console.WriteLine("------- PARAMETRY POZYCYJNE i NAZWANE -------");
            ITransaction tx5 = session1.BeginTransaction();
            IList<Produkt> produkty4 = session1.CreateQuery("from Produkt p where Id between ? and ? and Nazwa like :nazwa order by p.Nazwa asc")
                    .SetInt32(0, 1)
                    .SetInt32(1, 10)
                    .SetString("nazwa", "Banan__")
                    .List<Produkt>();
            foreach (var p in produkty4)
            {
                Console.WriteLine(p.Nazwa);
            }
            tx5.Commit();

            // Proste zapytanie
            Console.WriteLine("------- PROSTE ZAPYTANIE 1 -------");
            ITransaction tx6 = session1.BeginTransaction();
            IList<Koszyk> koszyki = session1.CreateQuery("from Koszyk k").List<Koszyk>();
            foreach (var k in koszyki)
            {
                Console.WriteLine("{0}, liczba towarów {1}", k.Klient, k.Produkty.Count);
            }
            tx6.Commit();

            // Mniej proste zapytanie
            Console.WriteLine("------- PROSTE ZAPYTANIE 2 -------");
            ITransaction tx7 = session1.BeginTransaction();
            IList<Produkt> produkty5 = session1.CreateCriteria(typeof(Produkt))
                    .CreateAlias("Koszyk", "Koszyk")
                    .Add(Expression.Or(
                        Expression.Le("Cena", 110.0),
                        Expression.Ge("Cena", 140.0)
                    ))
                    .Add(Expression.Like("Koszyk.Klient", "owal", MatchMode.Anywhere).IgnoreCase())
                    .AddOrder(Order.Asc("Cena"))
                    .List<Produkt>();
            Console.WriteLine(produkty5.Count);
            foreach (var p in produkty5)
            {
                Console.WriteLine("{0}: {1}", p.Nazwa, p.Cena);
            }
            tx7.Commit();

            Console.WriteLine("------- JOIN 1 -------");
            ITransaction tx8 = session1.BeginTransaction();
            var result = session1.CreateQuery("select k.ID, k.Klient, p.ID, p.Nazwa from Koszyk k join k.Produkty p").SetMaxResults(10).List();

            foreach (var r in result)
            {
                int KoszykID = (int)((object[])r)[0];
                string KoszykKlient = (string)((object[])r)[1];
                int ProduktID = (int)((object[])r)[2];
                string ProduktNazwa = (string)((object[])r)[3];
                Console.WriteLine("{0} {1} {2} {3}", KoszykID, KoszykKlient, ProduktID, ProduktNazwa);
            }
            tx8.Commit();

            Console.WriteLine("------- JOIN 2 -------");
            ITransaction tx9 = session1.BeginTransaction();
            var result2 = session1.CreateQuery("from Koszyk k join k.Produkty p").SetMaxResults(10).List();

            foreach (var r in result2)
            {
                var o = new
                {
                    Koszyk = (Koszyk)((object[])r)[0],
                    Produkt = (Produkt)((object[])r)[1]
                };
                Console.WriteLine("{0} {1}", o.Koszyk.Klient, o.Produkt.Nazwa);
            }
            tx9.Commit();

            Console.WriteLine("------- GRUPOWANIE -------");
            ITransaction tx10 = session1.BeginTransaction();
            var q1 = session1.CreateQuery(@"
                select k.ID as KoszykID, k.Klient as KoszykKlient, sum( p.Cena ) as Suma, count( p ) as Liczba
                from Koszyk k join k.Produkty p
                group by k.ID, k.Klient
                having count( p ) > 10
                order by sum( p.Cena ) desc, k.Klient asc, count( p ) desc
                ");

            var q = session1.CreateQuery(@"select p.Cena, sum(p.Cena)/12.0 as Srednia from Produkt p group by p.Cena order by count(p.Nazwa) desc");

            var result3 = q.SetMaxResults(10).List();

            foreach (var r in result3)
            {
                Dictionary<string, object> dane = new Dictionary<string, object>();
                for (int i = 0; i < q.ReturnAliases.Length; ++i)
                    dane.Add(q.ReturnAliases[i], ((object[])r)[i]);
                foreach (var c in dane)
                    Console.Write("{0} ", c.Value.ToString());
                Console.WriteLine();
            }
            tx10.Commit();

            Console.WriteLine("------- QBE -------");
            ITransaction tx11 = session1.BeginTransaction();

            Produkt sp = new Produkt { Nazwa = "Banan12" };
            ICriteria criteria = session1.CreateCriteria(typeof(Produkt));
            criteria.Add(Example.Create(sp)
                .ExcludeZeroes()
                //.ExcludeProperty("Cena")
                .EnableLike()
                .IgnoreCase());
            IList<Produkt> result4 = criteria.List<Produkt>();

            foreach (var r in result4)
            {
                Console.WriteLine("{0} {1}, {2}", r.Nazwa, r.Cena, r.Koszyk.Klient);
            }
            tx11.Commit();

            Console.WriteLine("------- LINQ -------");
            ITransaction tx12 = session1.BeginTransaction();

            var result5 = from k in session1.Query<Koszyk>()
                          select k;

            foreach (var r in result5)
            {
                Console.WriteLine("{0} {1}", r.Klient, r.Produkty.Count);
            }
            tx12.Commit();

            Console.WriteLine("------- QueryOver -------");
            ITransaction tx13 = session1.BeginTransaction();

            var result6 = session1.QueryOver<Koszyk>().List();

            foreach (var r in result6)
            {
                Console.WriteLine("{0} {1}", r.Klient, r.Produkty.Count);
            }
            tx13.Commit();

            session1.Close();

        }
    }
}
