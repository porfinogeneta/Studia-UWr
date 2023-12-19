namespace Ecommerce.Infrastructure.Repositories
{
    // trzeba by było jeszcze zmienić żeby pola w agragatach tam gdzie jest ID, było tylko ID
    public abstract class InMemoryRepositoryBase<T, G>
    {
        protected readonly List<T> entities = new List<T>();

        public T GetById(G id)
        {
            return entities.FirstOrDefault(o => o.ID == id);
        }

    }
}