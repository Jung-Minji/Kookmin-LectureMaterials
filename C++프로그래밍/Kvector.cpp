#include <iostream>
// #include "Kvector.h"
using namespace std;

template <class T>
class Kvector{
protected:
  T *m;
  int len;
public:
  Kvector(int sz = 0, T value = 0);
  Kvector(const Kvector& v);
  T sum() const{
    T s = 0;
    for(int i=0; i<len; i++) {
      s += m[i];
    }
    return s;
  }
virtual ~Kvector();
virtual void print() const
{
  cout << "Kvector: ";
  for(int i=0; i<len; i++) cout << m[i] << " ";
  cout << endl;
}
  void clear(){delete[] m; m = NULL; len = 0;}
  int size() const {return len;}
Kvector& operator=(const Kvector& v);
friend bool operator==(const Kvector& v, const Kvector& w)
{
  if(v.len != w.len) return false;
  for(int i=0; i<v.len; i++)
    if(v.m[i] != w.m[i]) return false;
  return true;
}
friend bool operator!=(const Kvector& v, const Kvector& w)
{
  return !(v==w);
}

T& operator[](int idx){ return m[idx]; }
const T& operator[](int idx) const { return m[idx]; }
friend std::ostream& operator<<(ostream& os, const Kvector& v)
{
  for(int i=0; i<v.size(); i++){
    os << v.m[i] << " ";
  }
  return os;
}
};

template<class T>
Kvector<T>::Kvector(int sz, T value): len(sz){
  cout << this << " : Kvecetor(" << sz << "," << value << ")\n";
  if (!sz){ m = NULL; return; }
  m = new T[sz];
  for(int i=0; i<sz; i++) m[i] = value;
}
template<class T>
Kvector<T>::Kvector(const Kvector& v){
  cout << this << " : Kvector(*" << &v << ")\n";
  len = v.len;
  if (!len) {m = NULL; return;}
  m = new int[len];
  for(int i=0; i<len; i++) m[i] = v.m[i];
}
template<class T>
Kvector<T>::~Kvector(){
  cout << this << " : ~Kvector() \n";
  delete[] m;
}
template<class T>
Kvector<T>& Kvector<T>::operator=(const Kvector& v) {
  cout << "Kvector::operator= " << &v << endl;
  delete[] m;
  len = v.len;
  m = new int[len];
  for(int i=0; i<len; i++) m[i] = v.m[i];
  return *this;
}

template <typename T>
void operator+=(const T& t1, const T& t2)
{
  t1 += t2;
  return t1;
}

int main(){
  Kvector<int> v1(3, 0); v1.print();
  cout << "v1 : " << v1 << endl;
  cout << "v1.sum() = " << v1.sum() << endl;

  Kvector<int *> v4(5, NULL); v4.print();
  int arr[5] = {0, 1, 2, 3, 4};
  for(int i=0; i<5; i++) v4[i] = &arr[4-i];
  cout << "v4 : " << v4 << endl;
  for(int i=0; i<5; i++) cout << *(v4[i]) << " ";
  cout << endl;
  return 0;
}
