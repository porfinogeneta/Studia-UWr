// tutaj zapisujemy sobie wyniki naszych agregacji

using Ecommerce.Domain;

namespace Ecommerce.Infrastructure;


class MemoryCustomerRepository : ICustomer
{
    private readonly List<CustomerDetails> customers = new List<CustomerDetails>();
    public GetDetails(int customerID)
    {
        return customers.FirstOrDefault(c => c.customer.CustomerId == customerID);
    }
}