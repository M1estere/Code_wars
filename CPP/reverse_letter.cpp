#include<iostream>
using namespace std;

std::string reverse_letter(const std::string s)
{
  string result_string = "";
  
  for (int i = 0; i < s.length(); i++)
  {
    if (isalpha(s[i]))
    {
      result_string = s[i] + result_string;
    } else
    {
      continue;
    }
  }

  return result_string;
}