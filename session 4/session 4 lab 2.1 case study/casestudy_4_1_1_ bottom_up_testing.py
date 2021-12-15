""" File Name: casestudy_4_1_1_ bottom_up_testing

Lab Activity: Lab 2_1

Author: sunil paudel
Student ID: s4664741
Date:09/09/2021

Program Description: doing bottonm-up testing for this progaram
:Read the TextAnalysis-CaseStudy provided on VU Collaborate Readings pages 126-130, then implement and test the program
as described in the case study. Take the screenshots of the testing
outputs.


Peer review student id and name :  Ankit bhujel (s4660565)

"""
#changing my working directry where my file is located.
import os
os.getcwd()
os.chdir('C:\\Users\\linus\\Desktop')
#Taking inputs from the user.
sentences= int(input("sentences: "))
words=int(input("words: "))
syllables=int(input("syllables: "))

#Calculation for flesch index

index=206.835-1.015*(words/sentences)-\
       84.6*(syllables/words)
#Output
print("flesch Index: ",index)
level=round(0.39*(words/sentences)+11.8*\
            (syllables/words)-15.59)
print("grade level:",level)
