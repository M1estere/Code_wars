using System;

class Arge {
    
    public static int NbYear(int p0, double percent, int aug, int p)
    {
        int yearsPassed = 0;

        while (p0 < p)
        {
            yearsPassed++;
            p0 = p0 + (int)(p0 * percent/100) + aug;
        }

        if (p0 >= p)
            return yearsPassed;
            
        return yearsPassed;
    }
}