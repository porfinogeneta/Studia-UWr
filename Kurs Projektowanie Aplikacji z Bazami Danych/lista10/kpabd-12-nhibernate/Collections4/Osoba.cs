using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

namespace Collections4
{
    public class Osoba
    {
        public int ID { get; set; }
        public string Imie { get; set; }
        public string Nazwisko { get; set; }
        public IList<string> Fotki { get; set; }
    }
}
