using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace FluentMapping
{
    public class Osoba
    {
        public virtual int ID { get; set; }
        public virtual string Imie { get; set; }
        public virtual string Nazwisko { get; set; }
        public override string ToString()
        {
            return string.Format("{0} {1}", Imie, Nazwisko);
        }
    }

}
