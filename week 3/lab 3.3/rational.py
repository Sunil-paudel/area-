"""File Name: rationaloperation.py
Lab Activity: Lab 3.3
Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 15/09/2021
Program Description:Implement and test the Rational Number Program (slides 9 and 10).Then, implement the Operation __add__, __sub__, __mul__
, __truediv__ for the Rational Operators. 
peer review: Name=  Samundra Rayamajhi Student id= s466370 """
class Rational(object): # creating class called Rational
    def __init__(self, numer, denom): # initiating the class with two attributes numer and denom
        self._numer = numer
        self._denom = denom

    def numberator(self):# defining numerator
        return self._numer

    def denominator(self): # defining denominator
        return self._denom

    def __str__(self): # for printing we are using this
        return str(self._numer) + "/" + str(self._denom)

    def __add__(self, other): # add function
        newNumber = self._numer * other._denom +\
                    other._numer * self._denom
        newDenom = self._denom * other._denom
        return Rational(newNumber, newDenom)

    def __mul__(self, other):# multiply function
        newNumber = self._numer * other._numer  
        newDenom = self._denom * other._denom
        return Rational(newNumber, newDenom)
    def __sub__(self, other): # substration fucntion
        newNumber = self._numer * other._denom -\
                    other._numer * self._denom
        newDenom = self._denom * other._denom
        return Rational(newNumber, newDenom)
    def __truediv__(self, other): # division function
        newNumber = self._numer * other._denom
        newDenom  = self._denom * other._numer
        return Rational(newNumber, newDenom)
# return is returning each function with rational nuber with numerator= newNumber and denominator as newdenom.
    
    









    



