public class Kata
{
    public static string OddOrEven(int[] array)
    {
        int arraySum = 0;
    
        for (int i = 0; i < array.Length; i++)
        {
            arraySum += array[i];
        }
    
        if (arraySum % 2 == 0)
            return "even";
        else
            return "odd";
    }
}