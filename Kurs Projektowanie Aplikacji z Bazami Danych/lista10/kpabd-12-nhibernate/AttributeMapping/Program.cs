using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NHibernate.Cfg;
using NHibernate.Mapping.Attributes;
using System.Reflection;
using NHibernate;
using System.Collections;
using System.IO;


namespace AttributeMapping
{
    class Program
    {
        static void Main( string[] args )
        {
            Configuration cfg = new Configuration();
            cfg.Configure();
            HbmSerializer.Default.Validate = true; // Opcjonalne
            // Here, we serialize all decorated classes (but you can also do it class by class)
            cfg.AddInputStream( HbmSerializer.Default.Serialize( Assembly.GetExecutingAssembly() ) );

            ISessionFactory f = cfg.BuildSessionFactory();
            using ( ISession s = f.OpenSession() )
            {
                Osoba o = new Osoba { Imie = "Jan", Nazwisko = "Kowalski" };
                s.Save( o );
                s.Flush();
                s.Close();
            }

            using ( ISession s = f.OpenSession() )
            {
                IList<Osoba> lista = s.CreateQuery( "from Osoba o order by o.Nazwisko" ).List<Osoba>();
                foreach ( var o in lista )
                    Console.WriteLine( "{0} {1}", o.Nazwisko, o.Imie );
                s.Close();
            }
        }
    }
}
