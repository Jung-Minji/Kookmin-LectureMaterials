#include <iostream>
#include "BitSet.h"
using namespace std;

BitSet::BitSet(int sz): Bvector(sz){
}
void BitSet::insert(int v){
  set(v);
}
BitSet operator+(const BitSet& v1, const BitSet& v2){
  if(v1.size() != v2.size()) throw IncompatibleException(v1.size(), v2.size());
  BitSet new_v(v1.size());
  for(int i=0; i<v1.size(); i++){
    if(v1.bit(i) == 1 || v2.bit(i) == 1){
      new_v.set(i);
    }
  }
  return new_v;
}
std::ostream& operator<<(std::ostream& os, const BitSet& s){
  os << "{ ";
  int idx = 0;
  for(int i=0; i<s.size(); i++){
    if(s.bit(i) == 1){
      cout << idx << " ";
    }
    idx++;
  }
  os << "}";
  return os;
}

int main(int argc, char* argv[]){
  BitSet b1(132), b2(131);
  b1.insert(3); b1.insert(5); b1.insert(8);
  b2.insert(4); b2.insert(5); b2.insert(8); b2.insert(130);
  b1.print(); b2.print();
  cout << "b1= " << b1 << endl;
  cout << "b2= " << b2 << endl;
  try{
    cout << "b1+b2= " << b1+b2 << endl;
  }
  catch(IncompatibleException& e){
    cout << "In + operation, the operands are note compatible.\n";
    cout << "The size of the first BitSet is " << e.v1_size << endl;
    cout << "The size of the second BitSet is " << e.v2_size << endl;
  }
}
