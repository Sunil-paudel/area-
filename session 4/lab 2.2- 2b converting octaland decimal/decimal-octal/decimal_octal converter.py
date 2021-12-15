"""
File Name: decimal_octalconverter.py
Lab Activity: Lab 2_1,2 b part1

Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 09/09/2021

Program Description: to convert decimal to octal
Peer review student id and name :  s4660565 Ankit Bhujel and s4663774 kshitij gurung

"""
#Taking decimal number input from the user
decimal = int(input("Enter a decimal integer: "))
if decimal == 0: 
    print(0)
else:
    print("Quotient Remainder ostring")
    ostring =""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        ostring = str(remainder) + ostring
        print("%5d%8d%12s" % (decimal, remainder, ostring))
    print("The octal representation is", ostring)
