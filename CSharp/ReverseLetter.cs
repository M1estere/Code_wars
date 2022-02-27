namespace myjinxin
{
    using System;
    
    public class Kata
    {
        public string ReverseLetter(string str)
        {
            str = str.ToLower();

            string alphabet = "abcdefghijklmnopqrstuvwxyz";

            string resultString = "";
            
            for (int i = 0; i < str.Length; i++)
            {
                if (alphabet.Contains(str[i]))
                {
                    resultString = str[i] + resultString;
                } else
                {
                    continue;
                }
            }

            return resultString;
        }
    }
}