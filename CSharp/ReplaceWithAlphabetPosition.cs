public static class Kata
{
    public static string AlphabetPosition(string text)
    {
        text = text.ToLower();

        string alphabet = "abcdefghijklmnopqrstuvwxyz";
            
        string resultString = "";

        for (int i = 0; i < text.Length; i++)
        {
            if (alphabet.Contains(text[i]))
            {
                resultString += alphabet.IndexOf(text[i]) + 1 + " ";
            } else
            {
                continue;
            }
        }

        return resultString.Trim();
    }
}