using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int GetUnique(IEnumerable<int> numbers)
    {

        for (int i = 0; i < numbers.Count(); i++)
        {
            if (numbers.Count(c => c.Equals(numbers.ElementAt(i))) == 1)
            {
                return numbers.ElementAt(i);
            }
        }

        return 0;
    }
}