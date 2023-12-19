using System.Collections.Generic;

namespace Associations1ManyToOne
{
    public class Stanowisko
    {
        public Stanowisko() { Osoby = new HashSet<Osoba>(); }
        public virtual int ID { get; set; }
        public virtual string Nazwa { get; set; }
        public virtual int Pensja { get; set; }
        public virtual ISet<Osoba> Osoby { get; set; }
    }
}
