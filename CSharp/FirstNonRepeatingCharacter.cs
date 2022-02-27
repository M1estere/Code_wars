public class Kata
{
    public static string FirstNonRepeatingLetter(string str)
    {
        string returnLetter = "";
            
        string tempString = str;
        tempString = tempString.ToLower();
    
        for (int i = 0; i < str.Length; i++)
        {
            if (tempString.LastIndexOf(tempString[i]) == tempString.IndexOf(tempString[i]))
            {
                returnLetter = str[i].ToString();
                break;
            } else
            {
                returnLetter = string.Empty;
            }
        }

        return returnLetter;
    }
}