#include<cmath>

bool isPrime(int num) {
  if (num == 0 || num == 1) 
    return false;

  int counter = 0;

  for (int i = 1; i <= sqrt(num); i++)
  {
    if (num % i == 0) 
      counter++;
    else
      continue;
  }

  if (counter == 1) 
    return true;

  return false;
}