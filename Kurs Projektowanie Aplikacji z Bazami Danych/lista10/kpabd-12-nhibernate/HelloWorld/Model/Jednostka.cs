namespace HelloWorld
{
    public class Jednostka
    {
        public virtual int ID { get; set; }
        public virtual string Nazwa { get; set; }
        public override string ToString()
        {
            return string.Format("{0} ({1})", Nazwa, ID.ToString());
        }
    }

}
