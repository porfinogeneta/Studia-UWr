/*
drop table if exists Ulica
go

create table Ulica
(
	Nazwa varchar(40),
	Miasto varchar(20),
	Zabytkowa bit
)
go
*/

using System;
using NHibernate;
using NHibernate.Cfg;

namespace CompositeKeys1
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }
        static void Main(string[] args)
        {
            ISession session1 = null;
            ISession session2 = null;
            var u = new Ulica { Nazwa = "Szewska", Miasto = "Wroclaw", Zabytkowa = true };

            try
            {
                session1 = OpenSession();
                ITransaction tx1 = session1.BeginTransaction();
                session1.SaveOrUpdate(u);
                tx1.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session1.Flush();
                session1.Close();
            }

            try
            {
                session2 = OpenSession();
                ITransaction tx2 = session2.BeginTransaction();

                Console.WriteLine("--------- Pierwszy sposób ---------");
                string SQL_QUERY = "from Ulica as u order by u.Nazwa asc";
                IQuery query = session2.CreateQuery(SQL_QUERY);
                Console.WriteLine("Znaleziono: {0}", query.List().Count);
                foreach (var o in query.List<Ulica>())
                    Console.WriteLine("Nazwa: {0}\t Miasto: {1}\t Czy zabytkowa: {2}",
                        o.Nazwa, o.Miasto, o.Zabytkowa ? "tak" : "nie");

                Console.WriteLine("--------- Drugi sposób ---------");
                //UlicaId uid = new UlicaId("Szewska", "Wroclaw");
                var u2 = new Ulica { Nazwa = "Szewska", Miasto = "Wroclaw" };
                u2 = session2.Get<Ulica>(u2);
                Console.WriteLine("Nazwa: {0}\t Miasto: {1}\t Czy zabytkowa: {2}",
                    u2.Nazwa, u2.Miasto, u2.Zabytkowa ? "tak" : "nie");

                tx2.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session2.Flush();
                session2.Close();
            }
            Console.ReadLine();
        }
    }
}