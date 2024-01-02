using Ecommerce.Domain.Models;

interface ICustomer
{
    Customer GetDetails(int customerID);
}