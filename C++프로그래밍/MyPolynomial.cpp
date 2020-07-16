#include "MyPolynomial.h"
#include <cmath>
//Constructor
myPolynomial::myPolynomial(int c, unsigned e): termNum(c, e){
degree = getDegree();
terms = new myTerm[termNum];
terms[0].setCoeff(c);
terms[0].setExp(e);
}
myPolynomial::myPolynomial(int nTerms, int mono[]){
this->nTerms = nTerms;
terms = new myTerm[nTerms];

int coeff[nTerms/2];
int exp[nTerms/2];

for(int i=0; i<nTerms; i++){
  if(i%2 == 0){
    exp[i] = nTerms[i];
  }
  else{
    coeff[i] = nTerms[i];
  }
}

for(int i=0; i<nTerms/2; i++){
  terms[i].setCoeff(coeff[nTerms/2-i]);
  terms[i].setExp(exp[nTerms/2-i]);
}
}

myPolynomial::myPolynomial(const myPolynomial &poly){
degree = poly.getDegree();
termNum = poly.getNumTerms();
terms = new myTerm[nTerms];
for(int i=0; i<nTerms; i++){
  terms = poly.terms[i];
}
}

// accessor, mutator functions
int myPolynomial::getDegree()const{
  return terms[0].getExp();
}
unsigned myPolynomial::getNumTerms() const{
  return nTerms;
}
int myPolynomial::getCoeff() const { return coeff; }

unsigned myPolynomial::getExp() const { return exp; }

void myPolynomial::setExp(unsigned e) {
   exp = e;
 }

void myPolynomial::setCoeff(int c){
  coeff = c;
}

//member functions
myPolynomial myPolynomial::ddx() const{
  myPolynomial d[nTerms];

  for(int i=0; i<nTerms; i++){
    d[i] = terms[i].ddx();
  }
  return d;
}

myPolynomial myPolynomial::operator+(const myPolynomial& poly) const{

}
myPolynomial myPolynomial::operator-(const myPolynomial& poly) const;
myPolynomial myPolynomial::operator*(const myPolynomial& poly) const;
myPolynomial myPolynomial::operator*(int vlaue) const{
  if(value == 0){
    return myPolynomial::ZERO;
  }
  myPolynomial re[nTerms];
  for(int i=0; i<nTerms; i++){
    re[i].setCoeff(getCoeff()*value);
  }
  return re;
}
myPolynomial operator*(int vlaue, const myPolynomial& poly){
  return value * poly;
}

long myPolynomial::operator()(int x) const{
  long result = 0;
  for(int i=0; i<nTerms; i++){
    result += terms[i].getCoeff*pow(x, terms[i].getExp());
  }
  return result;
}
myPolynomial myPolynomial::operator-() const {
  myPolynomial re[nTerms];
  for(int i=0; i<nTerms; i++){
    re[i] = -terms[i];
  }
  return re;
}
myPolynomial myPolynomial::operator-()const{
  myPolynomial re[nTerms];
  for(int i=0; i<nTerms; i++){
    re[i].setCoeff(terms[i].getCoeff()*-1);
  }
  return re;
}

bool myPolynomial::operator==(const myPolynomial &poly) const{
  if(nTerms != poly.nTerms) return false;
  for(int i=0; i<nTerms; i++){
    if(terms[i] != poly.terms[i]) return false;
  }
}
bool myPolynomial::operator!=(const myPolynomial &poly) const{
  return !(*this == poly);
}

myPolynomial& myPolynomial::operator+=(const myPolynomial &poly){
  *this += poly;
  return *this;
}
myPolynomial& myPolynomial::operator-=(const myPolynomial &poly){
  *this -= poly;
  return *this;
}
myPolynomial& myPolynomial::operator*=(const myPolynomial &poly){
  *this *= poly;
  return *this;
}
myPolynomial& myPolynomial::operator*=(int value){
  *this *= value;
  return *this;
}


// output operator
ostream& operator <<(ostream &outStream, const myPolynomial& poly)
{
bool check = true;
if (poly == myPolynomial::ZERO)
return outStream << 0;

outStream << poly.terms[0];
if(poly.terms[0].getCoeff() != 0) check = false;
for(int i=1; i<poly.nTerms; i++){
  if(poly.terms[i].getCoeff() != 0) check = false;

  if(poly.terms[i].getCoeff() > 0) outStream << '+';

  outStream << poly.terms[i];
}
if(check) return outStream << '0';
return outStream;
}

const myPolynomial myPolynomial::ZERO(0); // the zero polynomial P(x) = 0
const myPolynomial myPolynomial::ONE(1, (unsigned)0); // the monomial P(x) = 1
const myPolynomial myPolynomial::X(1, 1); // the monomial P(x) = x
