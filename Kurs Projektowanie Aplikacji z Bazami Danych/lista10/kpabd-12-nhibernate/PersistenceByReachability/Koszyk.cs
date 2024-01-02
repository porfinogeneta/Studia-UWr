using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PersistenceByReachability
{
    public class Koszyk
    {
        public Koszyk() { Atrybuty = new HashSet<string>(); Produkty = new HashSet<Produkt>(); }
        public int ID { get; set; }
        public string Klient { get; set; }
        public ISet<string> Atrybuty { get; set; }
        public ISet<Produkt> Produkty { get; set; }
    }
}
