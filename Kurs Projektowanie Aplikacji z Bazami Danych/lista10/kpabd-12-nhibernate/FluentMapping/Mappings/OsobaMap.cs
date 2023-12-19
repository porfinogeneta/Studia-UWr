using FluentNHibernate.Mapping;

namespace FluentMapping
{
    public class OsobaMap : ClassMap<Osoba>
    {
        public OsobaMap()
        {
            Id( x => x.ID );
            Map( x => x.Imie ).Length( 30 ).Not.Nullable();
            Map( x => x.Nazwisko ).Length( 30 ).Not.Nullable();
        }
    }
}
