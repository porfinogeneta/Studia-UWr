namespace Ecommerce.Domain.Models;

public class Order
{
    public int TransactionID { get; set; }
    public int CustomerID { get; set; }
    public List<int> ProductsIDs { get; set; }
    public Address ShippingAddress { get; set; }
}

public class Search
{
    public List<int> ProductsIDs { get; set; }
    public string Category { get; set; }

    public string productName { get; set; }
}

public class CustomerDetails
{
    public int customerID { get; set; }

    public Address address { get; set; }
}

public class ManageProduct
{
    public Product product { get; set; }

    public Decimal price { get; set; }
    public string category { get; set; }
    public string productName { get; set; }
}
