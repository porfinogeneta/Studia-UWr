using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Iesi.Collections.Generic;

namespace Associations2ManyToMany
{
    public class Ksiazka
    {
        public Ksiazka() { Kategorie = new HashSet<Kategoria>(); }
        public int ID { get; set; }
        public string Tytul { get; set; }
        public string Autor { get; set; }
        public ISet<Kategoria> Kategorie { get; set; }
    }
}
