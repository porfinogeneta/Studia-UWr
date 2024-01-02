using Ecommerce.Domain.Models;

class Search
{
    public List<Product> SearchProducts(string category = null, string name = null)
    {
        List<Product> results = new List<Product>
        {
            new Product(1, "product", 10, 2, true, "some")
        };

        return results;
    } 
}