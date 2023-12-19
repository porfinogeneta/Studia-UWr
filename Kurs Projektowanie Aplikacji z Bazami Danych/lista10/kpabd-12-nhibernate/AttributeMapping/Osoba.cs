using NHibernate.Mapping.Attributes;

namespace AttributeMapping
{
    [Class( Name = "AttributeMapping.Osoba, AttributeMapping", Lazy = false )]
    public class Osoba
    {
        [Id(Name="ID")]
        [Generator( 1, Class = "native" )]
        public virtual int ID { get; set; }
        [Property(Name="Imie")]
        public virtual string Imie { get; set; }
        [Property(Name="Nazwisko")]
        public virtual string Nazwisko { get; set; }
    }
}
