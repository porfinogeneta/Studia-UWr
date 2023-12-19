using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NHibernate;
using NHibernate.Cfg;

namespace IdentityMap
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
            ISession session3 = null;
            var os = new Osoba { Imie = "Jan", Nazwisko = "Kowalski" };

            try
            {
                session1 = OpenSession();
                ITransaction tx1 = session1.BeginTransaction();
                session1.SaveOrUpdate( os );
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

            Osoba p1 = null;
            Osoba p2 = null;
            Osoba p3 = null;
            try
            {
                session2 = OpenSession();
                p1 = session2.Load<Osoba>( 1 );
                p2 = session2.Load<Osoba>( 1 );

                if ( p1 == p2 )
                {
                    Console.WriteLine( "P1, P2 SA ROWNE" );
                }
                else
                {
                    Console.WriteLine( "P1, P2 NIE SA ROWNE" );
                }

                p1.Imie = "John";
                Console.WriteLine( "P2.Imie: " + p2.Imie );

                session3 = OpenSession();
                p3 = session3.Load<Osoba>( 1 );

                if ( p1 == p3 )
                {
                    Console.WriteLine( "P1, P3 SA ROWNE" );
                }
                else
                {
                    Console.WriteLine( "P1, P3 NIE SA ROWNE" );
                }
            }
            catch ( Exception e )
            {
                Console.WriteLine( e.Message );
            }
            finally
            {
                session2.Flush();
                session2.Close();
                session3.Flush();
                session3.Close();
            }
            Console.ReadLine();
        }
    }
}
