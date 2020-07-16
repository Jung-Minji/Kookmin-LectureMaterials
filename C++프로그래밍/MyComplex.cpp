#include "MyComplex.h"
// Constructor
myComplex::myComplex(int real, int imag)
{
realPart = real;
imaginaryPart = imag;
}
// Copy constructor
myComplex::myComplex(const myComplex& number)
{
realPart = number.realPart;
imaginaryPart = number.imaginaryPart;
}
// Accessor functions
int myComplex::getRealPart() const
{
return realPart;

}
int myComplex::getImaginaryPart() const
{
return imaginaryPart;
}
// Mutator functions
void myComplex::setRealPart(int real)
{
realPart = real;
}
void myComplex::setImaginaryPart(int imag)
{
imaginaryPart = imag;
}
void myComplex::set(int real, int imag)
{
realPart = real;
imaginaryPart = imag;
}
// Overloaded binary operators
myComplex myComplex::operator+(const myComplex& number) const
{
int newReal = realPart + number.realPart;
int newImag = imaginaryPart + number.imaginaryPart;
return myComplex (newReal, newImag);
}
myComplex myComplex::operator+(int value) const
{
return myComplex(value) + (*this);
}
myComplex operator+(int value, const myComplex& number)
{
return myComplex(value) + number;
}
myComplex myComplex::operator-(const myComplex& number) const
{
int newReal = realPart - number.realPart;
int newImag = imaginaryPart - number.imaginaryPart;
return myComplex (newReal, newImag);
}
myComplex myComplex::operator-(int value) const
{
return (*this) - myComplex(value);
}
myComplex operator-(int value, const myComplex& number)
{
return myComplex(value-number.realPart, -number.imaginaryPart);
}
myComplex myComplex::operator*(const myComplex& number) const
{
int newReal1 = realPart * number.realPart;  //ac
int newReal2 = realPart * number.imaginaryPart; // ad

int newImag1 = imaginaryPart * number.imaginaryPart; // bd
int newImag2 = imaginaryPart * number.realPart;//bc

return myComplex (newReal1-newImag1, newReal2 + newImag2);
}
myComplex myComplex::operator*(int value) const
{
return myComplex(value) * (*this);
}
myComplex operator*(int value, const myComplex& number)
{
return myComplex(value) * number;
}
// Assignment operators
myComplex& myComplex::operator=(const myComplex& number)
{
this->realPart = number.realPart;
this->imaginaryPart = number.imaginaryPart;
return *this;
}
myComplex& myComplex::operator=(int value)
{
realPart = value;
imaginaryPart = 0;
return *this;
}
myComplex& myComplex::operator+=(const myComplex& number)
{
this->realPart += number.realPart;
this->imaginaryPart += number.imaginaryPart;
return *this;
}
myComplex& myComplex::operator+=(int value)
{
realPart += value;
return *this;
}
myComplex& myComplex::operator-=(const myComplex& number)
{
this->realPart -= number.realPart;
this->imaginaryPart -= number.imaginaryPart;
return *this;
}
myComplex& myComplex::operator-=(int value)
{
realPart -= value;
return *this;
}
myComplex& myComplex::operator*=(const myComplex& number)
{
int resultReal = this->realPart*number.realPart - this->imaginaryPart*number.imaginaryPart; //ac - bd
int resultImag = this->realPart*number.imaginaryPart + this->imaginaryPart*number.realPart; //ad + bc
this->realPart = resultReal;
this->imaginaryPart = resultImag;
return *this;
}
myComplex& myComplex::operator*=(int value)
{
realPart *= value;
imaginaryPart *= value;
return *this;
}
// Overloading comparison operators
bool myComplex::operator==(const myComplex& number) const
{
return (realPart == number.realPart) &&
 (imaginaryPart == number.imaginaryPart);
}
bool myComplex::operator!=(const myComplex& number) const
{
return !(*this == number);
}
bool myComplex::operator>(const myComplex& number) const
{
return norm() > number.norm();
}
bool myComplex::operator<(const myComplex& number) const
{
return norm() < number.norm();
}
bool myComplex::operator>=(const myComplex& number) const
{
return (norm() >= number.norm());
}
bool myComplex::operator<=(const myComplex& number) const
{
return (norm() <= number.norm());
}

// Overloaded unary operators
myComplex myComplex::operator-() // unary minus
{
return myComplex(-realPart, -imaginaryPart);
}

myComplex& myComplex::operator--()
{
realPart--;
return *this;
}
myComplex myComplex::operator--(int)
{
myComplex t(*this);
operator--();
return t;
}
myComplex& myComplex::operator++()
{
realPart++;
return *this;
}
myComplex myComplex::operator++(int)
{
myComplex t(*this);
operator++();
return t;
}
myComplex myComplex::operator~(){
return myComplex(realPart, -imaginaryPart);
}

// private function
int myComplex::norm() const
{
return realPart * realPart + imaginaryPart * imaginaryPart;
}
ostream &operator <<(ostream &outStream, const myComplex& number)
{
outStream << "(" << number.realPart << "," << number.imaginaryPart << ")";
return outStream;
}
istream &operator >>(istream &inStream, myComplex& number)
{
inStream >> number.realPart >> number.imaginaryPart;
return inStream;
}
