using Ecommerce.Domain;

namespace Ecommerce.Infrastructure;

public class SearchRepository : ISearch
{
    private readonly List<Search> searches = new List<Search>();

    public List<Product> SeachGivenCategoryAndName(string query)
    {
         List<Product> result = searches.Where(s => s.category || s.name == query);
         return result;
    }
}