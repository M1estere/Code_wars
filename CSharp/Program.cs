using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Linq;

namespace CodeWars
{
    public class Program
    {
        
        private static void Main(string[] args)
        {
            /*
            Console.Write("Enter your word: ");
            string word = Console.ReadLine();

            Console.WriteLine($"Your Result: {DuplicateEncode(word)}"); */
            
            /*Console.WriteLine($"Result: {Find(new int[] {int.MaxValue, 0, 1})}");*/
            
            /*Console.WriteLine($"Result: {NbYear(1000, 2, 50, 1200)}");*/
            
            /*Console.WriteLine($"Result: {Solution("abc", "abc")}");*/
            
            /*int[] temp = SortArray(new int[] {5, 8, 6, 3, 4}); // 7 3 6 1
            Array.ForEach(temp, Console.WriteLine);*/
            
            /*Console.WriteLine($"Result: {FirstNonRepeatingLetter("sTresst")}");*/
            
            /*Console.WriteLine($"Result: {GetUnique(new [] {1, 1, 1, 2, 1, 1})}");*/

            /*Console.WriteLine($"Result: {Likes(new string[] {})}");*/
            
            /*Console.WriteLine($"Result: {GetReadableTime(7357)}");*/
            
            /*Console.WriteLine($"Result: {IsPrime(97)}");*/
        }
        
        #region FirstDay
        public static string DuplicateEncode(string word)
        {
            word = word.ToLower();
            
            string uniqueChars = "";
            for (int i = 0; i < word.Length; i++)
            {
                if (word.LastIndexOf(word[i]) == word.IndexOf(word[i]))
                {
                    uniqueChars += '(';
                }
                else
                {
                    uniqueChars += ')';
                }
            }

            return uniqueChars;
        }

        public static int Find(int[] integers)
        {

            int evens = 0; // even
            int odds = 0; // odd
            int mainInt = 0;
            
            for (int i = 0; i < integers.Length; i++)
            {
                if (integers[i] % 2 == 0)
                    evens += 1;
                else
                    odds += 1;
            }
            
            if (evens == 1) // even
            {
                for (int i = 0; i < integers.Length; i++)
                {
                    if (integers[i] % 2 == 0)
                        mainInt = integers[i];
                }
            } 
            
            if (odds == 1)
            {
                for (int i = 0; i < integers.Length; i++)
                {
                    if (integers[i] % 2 != 0)
                        mainInt = integers[i];
                }
            }

            return mainInt;
        }
        
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
        #endregion
        
        #region SecondDay
        public static bool Solution(string str, string ending)
        {
            /*if (str.EndsWith(ending)) return true;*/
            
            int strLength = str.Length; // abc 3
            int endingLength = ending.Length; // bc 2

            if (endingLength > strLength) return false;
            
            int freeChars = strLength - endingLength; // a 1

            if (str.Substring(freeChars) == ending)
                return true;
            
            return false;
        }
        
        public static int[] SortArray(int[] array) // 3 7 6 1
        {
            int temp = 0;
            
            for (int i = 0; i < array.Length; i++)
            {
                if(array[i] % 2 == 0)
                    continue;

                for(int j = (i + 1); j < array.Length; j++)
                {
                    if(array[j] % 2 != 0)
                    {
                        if(array[i] > array[j]) // < - descending / > - ascending
                        {
                            temp = array[i];
                            array[i] = array[j];
                            array[j] = temp;
                        }
                    }
                }
            }

            return array;
        }
        
        public static string FirstNonRepeatingLetter(string str)
        {
            string returnLetter = "";

            string tempString = str;
            tempString = tempString.ToLower(); // stresst
            
            for (int i = 0; i < str.Length; i++)
            {
                if (tempString.IndexOf(tempString[i]) != tempString.LastIndexOf(tempString[i])) 
                {
                    returnLetter = string.Empty;
                } else
                {
                    returnLetter = str[i].ToString();
                    break;
                }
            }

            return returnLetter;
        }
        #endregion
        
        #region ThirdDay
        public static int GetUnique(IEnumerable<int> numbers)
        {

           for (int i = 0; i < numbers.Count(); i++)
           {
               if (numbers.Count(c => c.Equals(numbers.ElementAt(i))) == 1)
               {
                   return numbers.ElementAt(i);
               }
           }

           return 0;
        }
        #endregion
        
        #region FourthDay
        public static string Likes(string[] name)
        {
            if (name.Length == 0) return "no one likes this";
            
            switch (name.Length)
            {
                case 1:
                    return $"{name[0]} likes this";
                case 2:
                    return $"{name[0]} and {name[1]} like this";
                case 3:
                    return $"{name[0]}, {name[1]} and {name[2]} like this";
                default:
                    return $"{name[0]}, {name[1]} and {name.Length - 2} others like this";
            }
        }
        
        public static string GetReadableTime(int seconds)
        {
            if (seconds < 0 || seconds > 359999) return "99:59:59";
            if (seconds == 0) return "00:00:00";

            int hours = 0;
            int minutes = 0;
            
            if (seconds >= 3600)
            {
                hours = seconds / 3600;
                minutes = (seconds / 60) % 60;
                seconds = seconds - (hours * 3600) - (minutes * 60);
            } else
            {
                hours = 0;

                if (seconds >= 60)
                {
                    minutes = (seconds / 60) % 60;
                    seconds = seconds - (minutes * 60);
                } else
                {
                    minutes = 0;
                }
            }

            string stringHours = "";
            string stringMinutes = "";
            string stringSeconds = "";

            if (hours < 10)
                stringHours = '0' + hours.ToString();
            else
                stringHours = hours.ToString();    
            
            if (minutes < 10)
                stringMinutes = '0' + minutes.ToString();
            else
                stringMinutes = minutes.ToString();

            if (seconds < 10)
                stringSeconds = '0' + seconds.ToString();
            else
                stringSeconds = seconds.ToString();    
            
            return stringHours + ":" + stringMinutes + ":" + stringSeconds;
        }
        public static bool IsPrime(int n)
        {
            if (n == 1) return false;
            
            int counter = 0;

            for (int i = 1; i <= Math.Sqrt(n); i++)
            {
                if (n % i == 0) 
                    counter += 1;
                else
                    continue;
            }

            if (counter == 1) 
                return true;
            
            return false;
        }
        #endregion
    }
}