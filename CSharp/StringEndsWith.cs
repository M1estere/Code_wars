public class Kata
{
    public static bool Solution(string str, string ending)
    {
        /*if (str.EndsWith(ending)) return true;*/
    
        int strLength = str.Length;
        int endingLength = ending.Length;

        if (endingLength > strLength) return false;
    
        int freeChars = strLength - endingLength;

        if (str.Substring(freeChars) == ending)
            return true;
            
        return false;
    }
}