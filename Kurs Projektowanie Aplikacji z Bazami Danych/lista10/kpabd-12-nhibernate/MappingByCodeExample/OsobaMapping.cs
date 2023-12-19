using NHibernate.Mapping.ByCode;
using NHibernate.Mapping.ByCode.Conformist;

namespace MappingByCodeExample
{
    public class OsobaMapping : ClassMapping<Osoba>
    {
        public OsobaMapping()
        {
            Id(e => e.ID, g => g.Generator(Generators.Identity));
            Property(e => e.Imie);
            Property(e => e.Nazwisko);
        }
    }
}
