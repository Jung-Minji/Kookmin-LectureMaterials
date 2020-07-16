#include <iostream>
#include "Bvector.h"
class IncompatibleException : public std::exception{
public:
  int v1_size;
  int v2_size;
  IncompatibleException(int v1, int v2): v1_size(v1), v2_size(v2){}
};

class BitSet : public Bvector{
public:
  BitSet(int sz=32);
void insert(int v);
friend BitSet operator+(const BitSet& v1, const BitSet& v2);
friend std::ostream& operator<<(std::ostream& os, const BitSet& s);
};
