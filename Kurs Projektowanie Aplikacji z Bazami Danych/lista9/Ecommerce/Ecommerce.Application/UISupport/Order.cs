using Ecommerce.Domain.Models;

class OrderSuppor
{
    void PlaceOrder(Order order)
    {
        return;
    }

    void CancelOrder(Order order)
    {
        return;
    }

    public Order GetOrderById(int orderId)
    {
        return new Order
            {
                TransactionID = orderId,
                CustomerID = 1,
                ProductsIDs = new List<int> { 101, 102, 103 },
                ShippingAddress = new Address
                {
                    City = "Cityville",
                    ZipCode = "12345",
                    Region = "Lowe Silesia",
                    Country = "Poland",
                    Flat = 1,
                    Block = 2
                }
            };
    }


}