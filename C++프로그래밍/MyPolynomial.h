#ifndef _MYPOLYNOMIAL_H_
#define _MYPOLYNOMIAL_H_
#include <iostream>
#include <list>
#include "MyTerm.h"
using namespace std;
class myPolynomial
{
public:
myPolynomial(int c = 0, unsigned e = 0);
myPolynomial(int nTerms, int mono[]);

// copy constructor
myPolynomial(const myPolynomial &poly);

// accessor, mutator functions
int getDegree()const;
unsigned getNumTerms() const;
int getCoeff() const; 
unsigned getExp() const;
void setCoeff(int c);
void setExp(unsigned e);
//member functions
myPolynomial ddx() const;

// overloaded operators
myPolynomial operator+(const myPolynomial& poly) const;
myPolynomial operator-(const myPolynomial& poly) const;
myPolynomial operator*(const myPolynomial& poly) const;
myPolynomial operator*(int vlaue) const;
friend myPolynomial operator*(int vlaue, const myPolynomial& poly);

long operator()(int x) const;
myPolynomial operator-() const;

bool operator==(const myPolynomial &poly) const;
bool operator!=(const myPolynomial &poly) const;

myPolynomial& operator+=(const myPolynomial &poly);
myPolynomial& operator-=(const myPolynomial &poly);
myPolynomial& operator*=(const myPolynomial &poly);
myPolynomial& operator*=(int value);

friend ostream& operator <<(ostream &outStream, const myPolynomial& poly);

static const myPolynomial ZERO; // P(x) = 0
static const myPolynomial ONE; // P(x) = 1
static const myPolynomial X; // P(x) = x

private:
int degree;
int nTerms;
myTerm * terms;

};
#endif _MYPOLYNOMIAL_H_
