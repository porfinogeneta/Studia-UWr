using Ecommerce.Domain.Models;

interface IManageProduct
{
    public void Add(Decimal Price, string name, string category);
    public void Delete(int productID);
}