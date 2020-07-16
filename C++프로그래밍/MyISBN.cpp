#include <cstring>
#include <cctype>
#include <string>
#include "MyISBN.h"
#include <vector>
#include <sstream>
#include <iostream>
#include <cstdlib>
using namespace std;

vector<string> split(string str, char dlmr) {
    vector<string> internal;
    stringstream ss(str);
    string tmp;

    while (getline(ss, tmp, dlmr)) {
        internal.push_back(tmp);
    }

    return internal;
}
// constructors
MyISBN::MyISBN ()
{
isbn[0] = '\0';
}
MyISBN::MyISBN (char isbn_number[])
{
strcpy(isbn, isbn_number);
}

// utility functions
bool MyISBN::isCorrectNumber() const
{
if (isSyntaxValid() && isCheckSumValid())
return true;
else
return false;
}
// private functions
bool MyISBN::isSyntaxValid() const
{
  int count = 0;
  bool check = false;
  string str;

 int strIdx = 0;
 while(isbn[strIdx] != '\0'){
   str += isbn[strIdx];
   strIdx++;
 }

 //cout << str << endl;
 if(str.length() != 13) return false;


 // -의 개수
 for(int j=0; j<str.length(); j++){
   if (str[j] == '-') count++;
 }
 //cout << "count: " << count << endl;
 if(count != 3) {
   return false;
 }


 // 문자가 들어간 경우
 for(int j=0; j<str.length(); j++){
   if('9' < str[j] || str[j] < '0'){
     if(str[j] != 'X' && str[j] != '-'){
       return false;
     }
   }
 }

 string checkString;
 for(int j=0; j<str.length(); j++){
   if(str[j] != '-'){
     checkString += str[j];
   }
 }
 if (checkString.length() != 10){
   return false;
 }

 // 해당하는 숫자가 없는 경우
 for(int j=0; j<str.length(); j++){
   if(str[0] == '-'){
     return false;
   }
   if(check == true && str[j] == '-'){
     return  false;
   }
   if(str[j] == '-') {
     check = true;
   }
   if('0'<= str[j] <= '9'){
     check = false;
   }

 }


 // 자리수 초과
  vector <string> v = split(str, '-');
  if (v.size() != 4) return false;

   if(5 < v.at(0).length()){
     return false;
   }
   if(7 < v.at(1).length()){
     return false;
   }
   if(6 < v.at(2).length()){
     return false;
   }
   if(1 != v.at(3).length()){
     return false;
   }


  return true;
}
bool MyISBN::isCheckSumValid() const
{
  string str = isbn;
  int err = 10;
  int idx = 0;
  int sum = 0;
  while(1 < err){
    if(str[idx]!= '-'){
      sum += (isbn[idx] -'0') * err;
      err--;
    }
    idx++;
  }

  int checkSum = (sum/11 + 1) * 11 - sum;
  if (checkSum == 10 && str[str.length()-1] == 'X'){
    return true;
  }

 if(checkSum % 11 == 0 && str[str.length()-1] == '0'){
   return true;
 }

  if(checkSum != str[str.length()-1] - '0'){
     return false;
  }else{
    return true;
  }




}
