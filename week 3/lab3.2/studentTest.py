"""
File Name: studenttest.py
Lab Activity: Lab 3.2
Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 16/09/2021

Program Description: c)	Old-fashioned photographs from the nineteenth century are not quite black and white and not quite color, but seem to have shades of gray,
brown, and blue. This effect is known as sepia. Write and test a function named sepia that converts a color image to sepia. This function should first call grayscale
function to convert the color image to grayscale.
peer review: Parichhit Basnet
s4662952
Parichhit.basnet@live.vu.edu"""
from student import Student
a = input("enter the student name: ")
b = int(input("enter the number of subject in which you want to get mark: "))
s = Student(a, b)
for sco in range(b):
    count = sco + 1
    s.setScore(count, input("enter the marks in subject: "))
print(s)
print(s.getName())
s.setName(input("enter the changed name of student: "))
print(s)
