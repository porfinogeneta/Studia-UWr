using Ecommerce.Domain.Models;

interface ISearch
{
    List<Product> SeachGivenCategoryAndName(string query);
}