using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using Iesi.Collections.Generic;

namespace Collections5
{
    public class Osoba
    {
        public int ID { get; set; }
        public string Imie { get; set; }
        public string Nazwisko { get; set; }
        public ISet<Fotka> Fotki { get; set; }
    }
}
