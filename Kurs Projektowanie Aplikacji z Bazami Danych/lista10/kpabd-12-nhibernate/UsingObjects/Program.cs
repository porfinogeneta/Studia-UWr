/*
drop table if exists Osoba;
go

create table Osoba
(
	ID int primary key identity,
	Imie varchar(50),
	Nazwisko varchar(30),
	Haslo varchar(20)
)
go

select * from Osoba
go

delete Osoba;
*/

using System;
using NHibernate;
using NHibernate.Cfg;

namespace UsingObjects
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }
        static void Main(string[] args)
        {
            // Utrwalenie obiektu
            var session = OpenSession();
            var user = new Osoba { Imie = "John", Nazwisko = "Doe" };
            var user2 = new Osoba { Imie = "Ewa", Nazwisko = "Malinowski" };
            try
            {
                var tx = session.BeginTransaction();
                session.Save(user);
                session.Save(user2);
                tx.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session.Close();
            }

            // Aktualizacja stanu trwałego obiektu odłączonego
            var session2 = OpenSession();
            try
            {
                user.Haslo = "Tajne";
                var tx = session2.BeginTransaction();
                session2.Update(user);
                user.Imie = "Jan";
                tx.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session2.Close();
            }

            //Pobranie obiektu trwałego
            var session3 = OpenSession();
            try
            {
                //Transaction tx = session3.beginTransaction();
                int id = 1;
                var u = session3.Get<Osoba>(id);
                Console.WriteLine("{0} : {1} : {2} : {3}", u.ID, u.Imie, u.Nazwisko, u.Haslo);
                //tx.commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session3.Close();
            }

            // Aktualizacja obiektu trwałego
            var session4 = OpenSession();
            try
            {
                var tx = session4.BeginTransaction();
                int id = 1;
                var u = session4.Get<Osoba>(id);
                u.Imie = "John";
                tx.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session4.Close();
            }

            // Zmiana obiektu trwałego na ulotny
            var session5 = OpenSession();
            try
            {
                var tx = session5.BeginTransaction();
                int id = 1;
                var u = session5.Get<Osoba>(id);
                session5.Delete(u);
                tx.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session5.Close();
            }

            // Zmiana obiektu odłączonego na ulotny
            var session6 = OpenSession();
            try
            {
                var tx = session6.BeginTransaction();
                session6.Delete(user2);
                tx.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session6.Close();
            }
        }
    }
}
