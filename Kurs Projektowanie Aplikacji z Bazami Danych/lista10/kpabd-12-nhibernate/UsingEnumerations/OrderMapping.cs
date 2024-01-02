using NHibernate.Mapping.ByCode;
using NHibernate.Mapping.ByCode.Conformist;

namespace UsingEnumerations
{
    public class OrderMapping : ClassMapping<Order>
    {
        public OrderMapping()
        {
            Table("[Order]");
            Id(e => e.ID, m => m.Generator(Generators.Identity));
            Property(e => e.Customer);
            Property(e => e.Address);
            Property(e => e.Status, m => m.Type<OrderStatusType>());
        }
    }
}
