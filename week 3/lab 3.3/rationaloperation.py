
"""
File Name: rationaloperation.py
Lab Activity: Lab 3.3
Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 15/09/2021

Program Description:Implement and test the Rational Number Program (slides 9 and 10).
Then, implement the Operation __add__, __sub__, __mul__, __truediv__ for the Rational Operators

peer review: Name=  Samundra Rayamajhi
Student id= s466370
"""
#importing files from Rational class of rayional.py which is in same directory
from rational import Rational
# letting user courtesy to input their own data
a = int(input("enter the first numerator:"))
b = int(input("enter the first denomenator:"))
c = int(input("enter the other numerator:"))
d = int(input("enter the other denomenator:"))
# using Rational class to give rational number
A = Rational(a, b)
B = Rational(c, d)
C = A + B # adding two rational number accroding to class Rational
D = A - B #subtracting two rational number accroding to class Rational
E = A * B #multiplying two rational number accroding to class Rational
F = A / B #dividing two rational number accroding to class Rational
# printing the output
print("the addition of data is",C)
print("the substarction of data is",D)
print("the multiplication  of data is",E)
print("the division of data is",F)
