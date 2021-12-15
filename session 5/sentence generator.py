""" File Name: sentencegenerator.py
Lab Activity: Lab 2_1
Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 09/09/2021
discription:Modify the sentence-generator program created in part 1 so that it inputs its vocabulary from a set of text files at startup.
The filenames are nouns.txt, verbs.txt, articles.txt, and prepositions.txt.
Peer review student id and name :  s4660565 Ankit Bhujel."""
import random
# Implementation of getWords method
def getWords(filename):
    #open the file in read mode
    readFile = open(filename,"r")
    #Declare the temporaryList
    temporaryList = list()
    #Iterate the loop
    for line in readFile:
        line = line.strip()
        #add to the temporaryList
        temporaryList.append(line)
    #convert the list into tuple
    allwords = tuple(temporaryList)
    #close the file
    readFile.close()
    #return the allwords
    return allwords
#Get the articles from getWords method
articles = getWords('articles.txt')
#Get the nouns from getWords method
nouns = getWords('nouns.txt')
#Get the verbs from getWords method
verbs = getWords('verbs.txt')
#Get the prepositions from getWords method
prepositions = getWords('prepositions.txt')
#Implementation of sentence method
def sentence():
    return nounPhrase() + " " + verbPhrase()
#Implementation of nounPhrase method
def nounPhrase():
    #return the random elements from articles and nouns
    return random.choice(articles) + " " + random.choice(nouns)
#Implementation of verbPhrase method
def verbPhrase():
    #return the random elements from verbs
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
#Implementation of prepositionalPhrase method
def prepositionalPhrase():
    #return the random elements from prepositions
    return random.choice(prepositions) + " " + nounPhrase()
#Implementation of main method
def main():
    #Get the number of sentence from user
    number = int(input('Enter number of sentences: '))
    #Iterate the loop
    for count in range(number):
        #Display statement
        print(sentence())
if __name__=='__main__':
    #call main method
    main()
