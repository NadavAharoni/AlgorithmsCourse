namespace sorting
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> list = new List<int>() { 23, 26, 4, -5, 12, 35, 122 };
            list.Add(17);
            list.Add(26);
            list.Add(39);

            for (int i = 0; i < list.Count-1; i++)
            {
                Console.Write($"{list[i]} ");
            }
            Console.WriteLine($"{list[list.Count - 1]}");
            Console.WriteLine($"{list.Count}");
        }
    }
}
