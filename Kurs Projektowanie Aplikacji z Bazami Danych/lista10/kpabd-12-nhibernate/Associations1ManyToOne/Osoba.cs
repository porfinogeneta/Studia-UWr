using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Iesi.Collections.Generic;

namespace Associations1ManyToOne
{
    public class Osoba
    {
        public virtual int ID { get; set; }
        public virtual string Imie { get; set; }
        public virtual string Nazwisko { get; set; }
        public virtual Stanowisko Stanowisko { get; set; }
    }
}
