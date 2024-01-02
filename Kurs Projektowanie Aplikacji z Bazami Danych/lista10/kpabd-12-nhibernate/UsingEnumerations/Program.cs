/*
drop table if exists [Order];
go

create table [Order]
(
	[ID] int primary key identity,
	[Customer] varchar(100),
	[Address] varchar(150),
	[Status] varchar(100)
)
go
*/

using System;
using System.Linq;
using NHibernate;
using NHibernate.Cfg;
using NHibernate.Mapping.ByCode;
using NHibernate.Linq;

namespace UsingEnumerations
{
    class Program
    {
        static void Main(string[] args)
        {
            var mapper = new ModelMapper();
            mapper.AddMapping(typeof(OrderMapping));
            var hbmMappings = mapper.CompileMappingForAllExplicitlyAddedEntities();
            Configuration configuration = new NHibernate.Cfg.Configuration().Configure();
            configuration.AddMapping(hbmMappings);
            ISessionFactory sessionFactory = configuration.BuildSessionFactory();

            using (var session = sessionFactory.OpenSession())
            {
                var o = new Order { Customer = "IBM", Address = "USA", Status = OrderStatus.InTravel };
                session.Save(o);
                session.Flush();
            }

            using (var session = sessionFactory.OpenSession())
            {
                var orders = from o in session.Query<Order>()
                             select o;
                foreach (var o in orders.ToList())
                {
                    Console.WriteLine("{0} {1} {2}", o.Customer, o.Address, OrderStatusType.GetDescription(o.Status));
                }
            }
            Console.ReadLine();
        }
    }
}
