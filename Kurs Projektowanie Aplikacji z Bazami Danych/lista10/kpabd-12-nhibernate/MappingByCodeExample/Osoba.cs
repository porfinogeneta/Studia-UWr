using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MappingByCodeExample
{
    public class Osoba
    {
        public virtual int ID { get; set; }
        public virtual string Imie { get; set; }
        public virtual string Nazwisko { get; set; }
    }
}
