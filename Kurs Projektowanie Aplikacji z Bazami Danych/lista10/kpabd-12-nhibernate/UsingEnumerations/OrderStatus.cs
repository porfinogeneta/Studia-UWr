using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UsingEnumerations
{
    public enum OrderStatus
    {
        InCompletion,
        Ready,
        InTravel,
        Delivered
    }

    public class OrderStatusType : NHibernate.Type.EnumStringType<OrderStatus>
    {
        public static string GetDescription(OrderStatus statusOferty)
        {
            switch (statusOferty)
            {
                case OrderStatus.InCompletion: return "W kompletowaniu";
                case OrderStatus.Ready: return "Gotowa do wysłania";
                case OrderStatus.InTravel: return "Wysłana";
                case OrderStatus.Delivered: return "Dostarczona";
                default: return string.Empty;
            }
        }
    }
}
