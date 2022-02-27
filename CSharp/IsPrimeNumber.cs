using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static bool IsPrime(int n)
    {
        if (n == 1) return false;
            
        int counter = 0;

        for (int i = 1; i <= Math.Sqrt(n); i++)
        {
            if (n % i == 0) 
                counter += 1;
            else
                continue;
        }

        if (counter == 1) 
            return true;
            
        return false;
    }
}