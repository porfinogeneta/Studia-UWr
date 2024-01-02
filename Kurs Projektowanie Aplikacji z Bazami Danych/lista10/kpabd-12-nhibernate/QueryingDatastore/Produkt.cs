namespace QueryingDatastore
{
    public class Produkt
    {
        public int ID { get; set; }
        public string Nazwa { get; set; }
        public double Cena { get; set; }
        public Koszyk Koszyk { get; set; }
    }
}
