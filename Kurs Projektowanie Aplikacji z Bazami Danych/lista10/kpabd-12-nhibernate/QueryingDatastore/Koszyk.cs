using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace QueryingDatastore
{
    public class Koszyk
    {
        public Koszyk() { Produkty = new HashSet<Produkt>(); }
        public int ID { get; set; }
        public string Klient { get; set; }
        public ISet<Produkt> Produkty { get; set; }
    }
}
