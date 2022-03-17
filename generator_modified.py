# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:51:13 2022

@author: user
"""

import random


def getWords(filename):


    readFile = open(filename,"r")


    temporaryList = list()


    for line in readFile:

        line = line.strip()

        temporaryList.append(line)

    wordsFinal = tuple(temporaryList)

    readFile.close()

    return wordsFinal


articles = getWords('articles.txt')

nouns = getWords('nouns.txt')

verbs = getWords('verbs.txt')

prepositions = getWords('prepositions.txt')

def sentence():

    return nounPhrase() + " " + verbPhrase()

def nounPhrase():

    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():

    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():

    return random.choice(prepositions) + " " + nounPhrase()

def main():


    number = int(input('Enter number of sentences: '))

    for count in range(number):

        print(sentence())

if __name__=='__main__':


    main()