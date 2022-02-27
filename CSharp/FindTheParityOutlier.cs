using System.Collections.Generic;
using System.Linq;
using System;

public class Kata
{
    public static int Find(int[] integers)
    {
        int evens = 0;
        int odds = 0;
    
        int result = 0;
            
        for (int i = 0; i < integers.Length; i++)
        {
            if (integers[i] % 2 == 0)
                evens += 1;
            else
                odds += 1;
        }
            
        if (evens == 1)
        {
            for (int i = 0; i < integers.Length; i++)
            {
                if (integers[i] % 2 == 0)
                    result = integers[i];
            }
        } 
            
        if (odds == 1)
        {
            for (int i = 0; i < integers.Length; i++)
            {
                if (integers[i] % 2 != 0)
                    result = integers[i];
            }
        }

        return result;
    }
}