using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Iesi.Collections.Generic;

namespace FetchingStrategies
{
    public class Produkt
    {
        public Produkt() { Atrybuty = new HashSet<Atrybut>(); }
        public virtual int ID { get; set; }
        public virtual string Nazwa { get; set; }
        public virtual double Cena { get; set; }
        public virtual Koszyk Koszyk { get; set; }
        public virtual ISet<Atrybut> Atrybuty { get; set; }

    }
}
