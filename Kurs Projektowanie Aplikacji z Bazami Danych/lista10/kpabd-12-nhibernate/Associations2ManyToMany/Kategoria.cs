using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Iesi.Collections.Generic;

namespace Associations2ManyToMany
{
    public class Kategoria
    {
        public Kategoria() { Ksiazki = new HashSet<Ksiazka>(); }
        public int ID { get; set; }
        public string Nazwa { get; set; }
        public ISet<Ksiazka> Ksiazki { get; set; }
    }
}
