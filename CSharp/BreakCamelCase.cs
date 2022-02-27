public class Kata
{
    public static string BreakCamelCase(string str)
    {
    
        string upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
        string resultString = "";
    
        for (int i = 0; i < str.Length; i++)
        {
            if (!upperAlphabet.Contains(str[i]))
            {
                resultString += str[i];
            } else 
            {
                resultString = resultString + ' ' + str[i]; 
            }
        }
    
        return resultString;
    }
}