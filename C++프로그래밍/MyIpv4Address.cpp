#include "MyIpv4Address.h"
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

// constructors
MyIpv4Address::MyIpv4Address ()
: addNumber(0)
{
num2address();
}
MyIpv4Address::MyIpv4Address (unsigned int num)
: addNumber(num)
{
num2address();
}
MyIpv4Address::MyIpv4Address (char add[])
{
string2address(add);
address2num();
}
// utility functions
void MyIpv4Address::printAddress() const
{
  for(int i=0; i<4; i++){
     cout << address[i];
     if(i != 3) cout << ".";
  }
}
void MyIpv4Address::printNumber() const
{
  cout << addNumber << endl;
}
// private functions
void MyIpv4Address::num2address()
{
  address[0] = addNumber /  pow(2, 24);
  address[1] = addNumber /  pow(2, 16);
  address[2] = addNumber /  pow(2, 8);
  address[3] = addNumber;
}
void MyIpv4Address::address2num()
{
  addNumber += address[0] * pow(2, 24);
  addNumber += address[1] * pow(2, 16);
  addNumber += address[2] * pow(2, 8);
  addNumber += address[3];
}
void MyIpv4Address::string2address(char add[])
{
  int idx = 0;
  string s;
  int len = strlen(add);
  for(int i=0; i<len; i++){
    if(add[i] == '.'){
      address[idx] = atoi(s.c_str());
      s = "";
    }
    else{
      s += add[i];
    }
  }
  address[idx] = atoi(s.c_str());
}
