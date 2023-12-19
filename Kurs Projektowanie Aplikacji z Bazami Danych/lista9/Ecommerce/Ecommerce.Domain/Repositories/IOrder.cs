// interfejs, dlatego że w Domain nie mamy dostępu do bazy danych
// implementujemy metody agragacyjne
// najczęściej realizują zadania typu add/get/remove
using Ecommerce.Domain.Models;

namespace Ecommerce.Domain;
interface IOrder
{
    void Add(Order order);
    void Delete(Order order);
    Order GetById(int orderID);
}