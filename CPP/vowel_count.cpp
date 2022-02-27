#include <string>

using namespace std;

int getCount(const string input_str)
{
  string vowels = "aeiou";
  
  int num_vowels = 0;
  
  for (int i = 0; i < input_str.length(); i++)
  {
    for (int k = 0; k < vowels.length(); k++)
    {
      if (input_str[i] == vowels[k])
      {
        num_vowels++;
      } else
      {
        continue;
      }
    }
  }
  return num_vowels;
}