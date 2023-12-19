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
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NHibernate;
using NHibernate.Cfg;

namespace CompositeKeys2
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static void Main( string[] args )
        {
            ISession session1 = null;
            ISession session2 = null;
            var u = new Ulica() { ID = new UlicaID { Nazwa = "Szewska", Miasto = "Wroclaw" }, Zabytkowa = true };

            try
            {
                session1 = OpenSession();
                ITransaction tx1 = session1.BeginTransaction();
                session1.SaveOrUpdate( u );
                tx1.Commit();
            }
            catch ( Exception e )
            {
                Console.WriteLine( e.Message );
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
                UlicaID uid = new UlicaID { Nazwa = "Szewska", Miasto = "Wroclaw" };
                var u2 = session2.Load<Ulica>( uid );
                Console.WriteLine( "Nazwa: {0}\t Miasto: {1}\t Czy zabytkowa: {2}",
                    u2.ID.Nazwa, u2.ID.Miasto, u2.Zabytkowa ? "tak" : "nie" );
                tx2.Commit();
            }
            catch ( Exception e )
            {
                Console.WriteLine( e.Message );
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
