using System.Collections.Specialized;

namespace Ecommerce.Domain.Models;

public class Product
{
    public int ProductID { get; set; }
    public string Name { get; set; }
    public decimal Price { get; set; }

    public int Amount { get; set; }
    public bool InStock { get; set; }
    public string Category { get; set; }

    public Product(int productID, string name, decimal price, int amount, bool inStock, string category)
    {
        ProductID = productID;
        Name = name;
        Price = price;
        Amount = amount;
        InStock = inStock;
        Category = category; 
    }

    public enum Lifecycle
    {
        Bought,
        Packed,
        Delivered
    }
}

public class Customer
{
    public int CustomerID { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public List<Transaction> transactions { get; set; }


    public Customer(int customerID, string name, string email)
    {
        CustomerID = customerID;
        Name = name;
        Email = email;
        transactions = null;
    }

    public enum Lifecycle
    {
        Login,
        Logout,
        Delete
    }
}

public class Manager
{
    public int ManagerID { get; set; }
    public string Name { get; set; }
    public List<Product> CreatedProducts { get; set; }


    public Manager(int managerID, string name)
    {
        ManagerID = managerID;
        Name = name;
        CreatedProducts = null;
    }

    public enum Lifecycle
    {
        Login,
        Logout,
        Delete
    }
}

public class Transaction
{
    public int TransactionID { get; set; }
    public decimal Amount { get; set; }
    public string Currency { get; set; }

    public Transaction(int transactionID, decimal amount, string currency)
    {
        TransactionID = transactionID;
        Amount = amount;
        Currency = currency;
    }

    // powinien być enum
    public enum Lifecycle {
        Completed,
        Payed,
        Archived
    }
}