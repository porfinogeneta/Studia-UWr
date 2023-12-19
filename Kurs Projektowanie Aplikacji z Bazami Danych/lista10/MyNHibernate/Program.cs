using NHibernate;
using NHibernate.Cfg;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
namespace NHibernateWprowadzenie
{
    class Program
    {
        static void Main(string[] args)
        {
            NHibernateExample NHibernate = new NHibernateExample();
        }
    }
    class NHibernateExample
    {
        // Pola związane z NHibernate 
        private Configuration myConfiguration;
        private ISessionFactory mySessionFactory;
        private ISession mySession;
        private Car[] myInitialObjects;
        private Car[] myFinalObjects;
        public NHibernateExample()
        {
            Configuration();
            NextAction();
        }
        public void Configuration()
        {
            // sprawdzamy czy przy uruchamianiu aplikacje sesje są otwarte
            // jeżeli tak należy je zamknąć
            if (mySession != null && mySession.IsOpen)
            {
                mySession.Close();
            }
            if (mySessionFactory != null && !mySessionFactory.IsClosed)
            {
                mySessionFactory.Close();
            }
            // Inicjowanie NHibernate
            myConfiguration = new Configuration();
            myConfiguration.Configure();
            mySessionFactory = myConfiguration.BuildSessionFactory();
            mySession = mySessionFactory.OpenSession();
            // Przygotowanie przykładowanych danych
            PrepareCarData();
            Console.WriteLine("Konfiguracja przebiegła pomyślnie..");
            Console.WriteLine();
        }
        public void PrepareCarData()
        {
            myInitialObjects = new Car[2];
            myFinalObjects = new Car[2];
            // Dodajemy dwa samochody
            Car car1 = new Car();
            car1.Brand = "Audi";
            car1.Model = "100";
            car1.Price = 1000;
            myInitialObjects[0] = car1;
            Car car2 = new Car();
            car2.Brand = "Audi";
            car2.Model = "RS6";
            car2.Price = 2000;
            myInitialObjects[1] = car2;
        }
        // public void DeleteData()
        // {
        //     // Usunięcie wszystkich rekordów
        //     using (ISession session = mySessionFactory.OpenSession())
        //     {
        //         SqlConnection con = session.Connection as SqlConnection;
        //         SqlCommand cmd = new SqlCommand("Delete from Car", con);
        //         cmd.ExecuteNonQuery();
        //     }
        //     Console.WriteLine("Rezultat operacji: Dane zostały usunięte z tabeli Cars");
        //     Console.WriteLine();
        //     NextAction();
        // }
        public void DeleteSpecifiedData()
        {
            // Usunięcie wybranego rekordu
            using (mySession.BeginTransaction())
            {
                mySession.Delete(myInitialObjects[0]);
                mySession.Transaction.Commit();
            }
            Console.WriteLine("Rezultat operacji: Usnięto - Id: {0}, Marka: {1}, Model: {2}",
                myInitialObjects[0].ID, myInitialObjects[0].Brand, myInitialObjects[0].Model);
            Console.WriteLine();
            NextAction();
        }
        public void AddData()
        {
            // Dodanie wcześniej przygotowanych danych
            using (mySession.BeginTransaction())
            {
                mySession.Save(myInitialObjects[0]);
                mySession.Save(myInitialObjects[1]);
                mySession.Transaction.Commit();
            }
            Console.WriteLine("Rezultat operacji: Dane zostały poprawnie dodane do tabeli Cars");
            Console.WriteLine();
            NextAction();
        }
        public void GetAllData()
        {
            // Wyświetlenie wszystkich danych z tabeli Car
            using (mySession.BeginTransaction())
            {
                // Poniżej trworzymy kryteria pobierania danych z tabeli
                ICriteria criteria = mySession.CreateCriteria<Car>();
                IList<Car> list = criteria.List<Car>();
                // Gdybyśmy chcieli zdefiniować warunki wyszukiwania wystarczy zrobić to w poniższy sposób
                // IList<Car> list = criteria.List<Car>().Where(a => a.CarId > 3).ToList();
                foreach (var item in list)
                {
                    Console.WriteLine("Id: {0}, Marka: {1}, Model: {2}", item.ID, item.Brand, item.Model);
                }
                Console.WriteLine();
                NextAction();
            }
        }
        public void NextAction()
        {
            Console.WriteLine("Wybierz następne działanie, które chcesz wykonać: ");
            Console.WriteLine("1: Skasowanie danych z tabeli Car");
            Console.WriteLine("2: Dodanie danych do tabeli Car");
            Console.WriteLine("3: Wyświetlenie wszystkich danych z tabeli Car");
            Console.WriteLine("4: Opuścić aplikację: ");
            Console.Write("Twój wybór: ");
            int actionId = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine();
            switch (actionId)
            {
                case 1:
                    // DeleteData();
                    break;
                case 2:
                    AddData();
                    break;
                case 3:
                    GetAllData();
                    break;
                case 4:
                    System.Environment.Exit(0);
                    break;
                default:
                    break;
            }
            Console.ReadKey();
        }
    }
}
