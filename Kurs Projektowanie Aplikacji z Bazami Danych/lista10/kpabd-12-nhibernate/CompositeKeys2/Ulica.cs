using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CompositeKeys2
{
    public class UlicaID
    {
        public virtual string Nazwa { get; set; }
        public virtual string Miasto { get; set; }
        public override bool Equals( object o )
        {
            if ( o == null ) return false;
            if ( object.ReferenceEquals( this, o ) ) return true;
            var id = o as UlicaID;
            if ( id == null ) return false;

            return Nazwa == id.Nazwa && Miasto == id.Miasto;
        }
        public override int GetHashCode()
        {
            return Nazwa.GetHashCode() + 27 * Miasto.GetHashCode();
        }
    }
    public class Ulica
    {
        public virtual UlicaID ID { get; set; }
        public virtual bool Zabytkowa { get; set; }
    }
}
