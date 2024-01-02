using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CompositeKeys1
{
    public class Ulica
    {
        public virtual string Nazwa { get; set; }
        public virtual string Miasto { get; set; }
        public virtual bool Zabytkowa { get; set; }
        public override bool Equals(object o)
        {
            if (o == null) return false;
            if (object.ReferenceEquals(this, o)) return true;
            var id = o as Ulica;
            if (id == null) return false;

            return Nazwa == id.Nazwa && Miasto == id.Miasto;
        }
        public override int GetHashCode()
        {
            return Nazwa.GetHashCode() + 27 * Miasto.GetHashCode();
        }
    }
}
