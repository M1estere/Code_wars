using namespace std;

string get_middle(string input) 
{
  int input_length = input.length();
  
  auto pos = input.length() == 0 ? 0 : input_length / 2 - (input_length % 2 == 0);
  auto n = 1 + (input_length % 2 == 0);
  
  return input.substr(pos, n);
}