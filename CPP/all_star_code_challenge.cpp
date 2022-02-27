#include <iostream>
#include <string>

std::string to_time(unsigned seconds) 
{
  int hours = seconds / 3600;
  int minutes = (seconds / 60) % 60; 
  
  return std::to_string(hours) + " hour(s) and " + std::to_string(minutes) + " minute(s)";
}