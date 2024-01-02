using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace FetchingStrategies
{
    public class Atrybut
    {
        public virtual int ID { get; set; }
        public virtual string Wartosc { get; set; }
        public virtual Produkt Produkt { get; set; }
    }
}
