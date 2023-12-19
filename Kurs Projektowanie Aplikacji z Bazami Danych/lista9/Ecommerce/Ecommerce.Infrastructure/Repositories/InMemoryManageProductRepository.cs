using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using Ecommerce.Domain;

namespace Ecommerce.Infrastructure
{
    public class ManageProductRepository : IManageProduct
    {
        private readonly List<Product> products = new List<Product>();

        public void Add(decimal price, string name, string category)
        {
            Product product = new Product
            {
                ProductID = GenerateProductID(),
                Name = name,
                Price = price,
                Category = category,
                InStock = true
            };

            products.Add(product);
        }

        public void Delete(int productID)
        {
            Product productToRemove = products.Find(p => p.ProductID == productID);

            if (productToRemove != null)
            {
                products.Remove(productToRemove);
            }
            else
            {
                Console.WriteLine($"Product with ID {productID} not found.");
            }
        }

        private int GenerateProductID()
        {
            return products.Count + 1;
        }
    }
}
