using System;

public static class Kata 
{
    public static string ToUnderscore(int str)
    {
        return str.ToString();
    }

    public static string ToUnderscore(string str) 
    {
        string upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            
        string resultString = "";
            
        for (int i = 0; i < str.Length; i++)
        {
            if (upperAlphabet.Contains(str[i]) && i != 0)
            {
                resultString += "_" + str[i];
            } else
            {
                resultString += str[i];
            }
        }

        return resultString.ToLower();
    }
}