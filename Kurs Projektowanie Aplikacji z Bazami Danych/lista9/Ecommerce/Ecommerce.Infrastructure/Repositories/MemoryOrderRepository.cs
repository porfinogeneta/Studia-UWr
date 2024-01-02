
public class OrderRepository : IOrder
    {
        private readonly List<Order> orders = new List<Order>();

        public void Add(Order order)
        {
            orders.Add(order);
        }

        public void Delete(Order order)
        {
            orders.Remove(order);
        }

        public Order GetById(int orderID)
        {
            return orders.FirstOrDefault(o => o.TransactionID == orderID);
        }
    }
