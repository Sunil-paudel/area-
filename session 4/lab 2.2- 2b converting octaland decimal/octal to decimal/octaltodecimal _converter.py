"""
File Name: octaltodecimal_converter.py
Lab Activity: Lab 2_1 2.b part 2

Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 09/09/2021
Program Description: to convert octal to decimal

Peer review student id and name :  (s4660565) Ankit Bhujel and s4663774 kshitij gurung

"""
#Taking the octal value from the user
ostring=input("enter the octal value: ")
decimal=0
exponent= len(ostring) - 1

#Converting into decimal
for digit in ostring:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent = exponent - 1
#Output
print("The decimal value of ",(ostring), " is ", decimal)
