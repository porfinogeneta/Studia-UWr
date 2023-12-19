using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UsingEnumerations
{
    public class Order
    {
        public virtual int ID { get; set; }
        public virtual string Customer { get; set; }
        public virtual string Address { get; set; }
        public virtual OrderStatus Status { get; set; }
    }
}
