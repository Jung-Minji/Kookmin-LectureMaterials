#include <iostream>
#include <string>
#include <cassert>
using namespace std;
#define N 3

class Kvector{
protected:
  int *m;
  int len;
public:
  Kvector(int sz = 0, int value = 0);
  Kvector(const Kvector& v);
  friend bool operator==(const Kvector& k, const Kvector& d);
  friend ostream& operator<<(ostream& os, const Kvector& k);
  Kvector& operator=(const Kvector& k);
  int& operator[](int idx);
  ~Kvector(){
    cout << this << " : ~Kvector() \n";
    delete[] m;
  }

  void print(){
    for(int i=0; i<len; i++) cout << m[i] << " ";
    cout << endl;
  }

  void print() const{
    for(int i=0; i<len; i++) cout << m[i] << " ";
    cout << endl;
  }

  void clear(){
    delete [] m;
    m = NULL;
    len = 0;
  }
  int size() const {return len;}
};

Kvector::Kvector(int sz, int value){
  if (sz == 0){
    m = NULL;
    return;
  }
  m = new int[sz];
  for(int i=0; i<sz; i++) m[i] = value;
  len = sz;

  cout << this << " : " << "Kvector(int, int)" << endl;
}


Kvector::Kvector(const Kvector& v){
  m = new int[v.size()];
  for(int i=0; i<v.size(); i++) m[i] = v.m[i];
  len = v.size();

  cout << this << " : " << "Kvector(Kvector&)" << endl;
}

bool operator==(const Kvector& k, const Kvector& d){
  bool result = true;
  if (k.size() != d.size()){
    result = false;
  }
  else{
    for(int i=0; i<k.size(); i++){
      if (k.m[i] != d.m[i]){
        result = false;
        break;
      }
    }
  }
  return result;
}

bool operator!=(const Kvector& k, const Kvector& d){
  return !(k==d);
}

ostream& operator<<(ostream& os, const Kvector& k){
  for(int i=0; i<k.size(); i++){
    os << k.m[i] << " ";
  }
  return os;
}

Kvector& Kvector::operator=(const Kvector& k) {
  if (&k != this){
    delete[] m;
  m = new int[k.size()];
  for(int i=0; i<k.size(); i++) m[i] = k.m[i];
  }
  len = k.size();
  return *this;
}

int& Kvector::operator[](int idx){
  assert(0 <= idx && idx < size());
  return m[idx];
}

class Avector : public Kvector{
  char table[N];
public:
  Avector(int sz=0, int v=0, const char *t="abc"):Kvector(sz, v){
    for(int i=0; i<N; i++){
      table[i] = *t;
      t++;
    }
    cout << this << " : " << "Avector(int, int, const char*)" << endl;
    for(int i=0; i<N; i++)  cout << table[i];
    cout << endl;
  }

  void setTable(const char *t){
    for(int i=0; i<N; i++){
      table[i] = *t;
      t++;
    }
  }
friend ostream& operator<<(ostream& os, const Avector& v);
};
ostream& operator<<(ostream& os, const Avector& v){
  for(int i=0; i<v.len; i++){
    os << v.table[v.m[i]%3] << " ";
  }
  return os;
}



int main(int argc, char* argv[]){
  if(argc != 2){
    cout << "usage: ./avector pqr\n";
    return 1;
  }
  Avector v1(3); v1.print();
  Avector v2(2, 1, "xyz"); v2.print();
  Avector v3(v2); v3.print();
  cout << (v1 == v2) << endl;
  cout << (v3 == v2) << endl;
  v3 = v2 = v1;
  cout << v1 << endl;
  v1.print();
  cout << v2 << endl;
  v2.print();
  cout << v3 << endl;
  v3.print();
  cout << (v3 != v2) << endl;
  v1[2] = 2;
  v2[0] = v1[2];
  v1.setTable(argv[1]);
  cout << "v1: " << v1 << "v2: " << v2 << "v3: " << v3 << endl;
  v1.print();
  v2.print();
  v3.print();
  return 0;
}
