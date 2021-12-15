

"""
file:wage.py
Lab1.2quesetion 2
author:Sunil chandra paudel
student id:s4664741
Date:31 aug 2021
program discription:An employee’s total weekly pay equals the hourly wage multiplied
by the total number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage.
Write a program that takes as inputs the hourly wage, total regular hours, and total
overtime hours and displays an employee’s total weekly pay. 
Peer review student id and name-s4663902
ashsish sapkota

"""
#constants
#input
x=float(input("enter the hourly wage:"))
y=float(input("please fill in the regular hours in a week:"))
z=float(input("please fill in the overtime hoursin a week:"))
#process
A=x*y+z*(1.5*x)
#output
print("the total weekely wage is:", A)
