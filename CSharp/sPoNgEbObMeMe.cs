public class Kata
{
    public static string SpongeMeme(string sentence)
    {
        string resultString = "";
            
        for (int i = 0; i < sentence.Length; i++)
        {
            if (i % 2 == 0)
                resultString += char.ToUpper(sentence[i]);
            else
                resultString += char.ToLower(sentence[i]);
        }

        return resultString;
    }
}