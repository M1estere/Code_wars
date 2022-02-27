public class Kata
{
    public static string DuplicateEncode(string word)
    {
        word = word.ToLower();
            
        string uniqueChars = "";
    
        for (int i = 0; i < word.Length; i++)
        {
            if (word.LastIndexOf(word[i]) == word.IndexOf(word[i]))
            {
                uniqueChars += '(';
            } else
            {
                uniqueChars += ')';
            }
        }

        return uniqueChars;
    }
}