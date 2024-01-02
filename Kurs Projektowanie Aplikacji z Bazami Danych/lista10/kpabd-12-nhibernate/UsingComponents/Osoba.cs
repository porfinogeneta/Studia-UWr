using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace UsingComponents
{
    public class Osoba
    {
        public virtual int ID { get; set; }
        public virtual string Imie { get; set; }
        public virtual string Nazwisko { get; set; }
        public virtual Adres DomowyAdres { get; set; }
        public virtual Adres SluzbowyAdres { get; set; }
    }
}
