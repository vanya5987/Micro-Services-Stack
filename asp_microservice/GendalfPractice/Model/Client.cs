namespace GendalfPractice.Model
{
    public class Client
    {
        public long Id { get; set; }

        public string Name { get; set; } = string.Empty;

        public string Surname { get; set; } = string.Empty;

        public decimal Salary { get; set; }

        public DateTime BirthDay { get; set; }
    }
}
