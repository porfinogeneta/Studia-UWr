/*
drop table if exists Osoba;
go

create table Osoba
(
	ID int primary key identity,
	Imie varchar(30) not null,
	Nazwisko varchar(50) not null,
	UlicaDom varchar(100),
	MiastoDom varchar(100),
	UlicaPraca varchar(100),
	MiastoPraca varchar(100)
)
go
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NHibernate;
using NHibernate.Cfg;

namespace UsingComponents
{
    class Program
    {
        static ISession OpenSession()
        {
            return new Configuration().Configure().BuildSessionFactory().OpenSession();
        }
        static void Main(string[] args)
        {
            ISession session1 = null;
            ISession session2 = null;
            var domowyAdres = new Adres() { Ulica = "Grabiszyńska", Miasto = "Wrocław" };
            var sluzbowyAdres = new Adres() { Ulica = "Szczytnicka", Miasto = "Wrocław" };
            var osoba = new Osoba() { Imie = "Jan", Nazwisko = "Kowalski", DomowyAdres = domowyAdres, SluzbowyAdres = sluzbowyAdres };

            try
            {
                session1 = OpenSession();
                ITransaction tx1 = session1.BeginTransaction();
                session1.SaveOrUpdate(osoba);
                tx1.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session1.Flush();
                session1.Close();
            }

            try
            {
                session2 = OpenSession();
                ITransaction tx2 = session2.BeginTransaction();
                string SQL_QUERY = "from Osoba as o order by o.Nazwisko asc";
                IQuery query = session2.CreateQuery(SQL_QUERY);
                Console.WriteLine("Znaleziono: {0}", query.List().Count);
                foreach (var os in query.List<Osoba>())
                {
                    Console.WriteLine("ID: {0}\t Imie: {1}\t Nazwisko: {2}\t Ulica dom: {3}\t Ulica praca: {4}",
                        os.ID, os.Imie, os.Nazwisko, os.DomowyAdres.Ulica, os.SluzbowyAdres.Ulica);
                }

                tx2.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                session2.Flush();
                session2.Close();
            }
            Console.ReadLine();
        }
    }
}
