using System;
using System.Collections.Generic;
using System.Linq;

class ReverseLonger
{
    public static string ShorterReverseLonger(string a, string b)
    {
        char[] aArray = new char[] { };
        char[] bArray = new char[] { };
       
        if (a == null) a = string.Empty;
        if (b == null) b = string.Empty;
    
        if (a != string.Empty)
        {
            aArray = a.ToCharArray();
            Array.Reverse(aArray);
        }

        if (b != string.Empty)
        {
            bArray = b.ToCharArray();
            Array.Reverse(bArray);
        }
    
        return a.Length >= b.Length ? b + new string(aArray) + b : a + new string(bArray) + a;
    }
}