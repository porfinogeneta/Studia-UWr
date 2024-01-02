using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Transactions;
using NHibernate;
using NHibernate.Cfg;
using NHibernate.Mapping.ByCode;

namespace MappingByCodeExample
{
    class Program
    {
        static void Main(string[] args)
        {
            var mapper = new ModelMapper();
            mapper.AddMapping(typeof(OsobaMapping));
            var hbmMappings = mapper.CompileMappingForAllExplicitlyAddedEntities();
            Configuration configuration = new NHibernate.Cfg.Configuration().Configure();
            configuration.AddMapping(hbmMappings);
            ISessionFactory sessionFactory = configuration.BuildSessionFactory();

            using (var session = sessionFactory.OpenSession())
            {
                using (var scope = new TransactionScope())
                {
                    var o = new Osoba { Imie = "Jan", Nazwisko = "Kowalski" };
                    session.Save(o);
                    //scope.Complete();
                }

                using (var scope = new TransactionScope())
                {
                    var osoby = session.CreateCriteria(typeof(Osoba)).List<Osoba>();

                    foreach (var o in osoby)
                    {
                        Console.WriteLine(o.Nazwisko);
                    }
                }
            }
        }
    }
}
