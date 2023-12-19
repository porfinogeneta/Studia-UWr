using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NHibernate.Cfg;
using NHibernate;

namespace FactoryCreationCost
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }

        static ISessionFactory CreateFactory()
        {
            return new Configuration().Configure().BuildSessionFactory();
        }

        static void Main( string[] args )
        {
            int N = 500;
            Console.WriteLine( "Enter aby rozpocząć" );
            Console.ReadLine();
            Console.WriteLine( "Wiele fabryk" );
            DateTime t1 = DateTime.Now;
            for ( int i = 0; i < N; ++i )
            {
                Console.Write( "." );
                ISession s = OpenSession();
            }
            DateTime t2 = DateTime.Now;
            Console.WriteLine(); Console.WriteLine();
            Console.WriteLine( "Enter aby kontynuować" );
            Console.ReadLine();
            Console.WriteLine( "Jedna fabryka" );
            DateTime t3 = DateTime.Now;
            ISessionFactory factory = CreateFactory();
            for ( int i = 0; i < N; ++i )
            {
                Console.Write( "." );
                ISession s = factory.OpenSession();
            }
            DateTime t4 = DateTime.Now;
            Console.WriteLine();
            Console.WriteLine( ( t2 - t1 ).Milliseconds );
            Console.WriteLine( ( t4 - t3 ).Milliseconds );
            Console.ReadLine();
        }
    }
}
