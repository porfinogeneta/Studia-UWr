using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Iesi.Collections.Generic;

namespace FetchingStrategies
{
    public class Koszyk
    {
        public Koszyk() { Produkty = new HashSet<Produkt>(); }
        public virtual int ID { get; set; }
        public virtual string Klient { get; set; }
        public virtual ISet<Produkt> Produkty { get; set; }
    }
}
