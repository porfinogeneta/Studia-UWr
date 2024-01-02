namespace Ecommerce.Domain.Models;

public class Price
{
    public decimal Amount { get; set; }
    public string Currency { get; set; }
}

public class Address
{
    public string Country { get; set; }
    public string ZipCode { get; set; }
    public string Region { get; set; }
    public string City { get; set; }
    public int Block { get; set; }
    public int Flat { get; set; }
}