# File: WordleAssistant.py
# Student: Danielle Balque
# UT EID: dsb2643
# Course Name: CS303E
# 
# Date: 11/5/2022
# Description of Program: This program computes Wordle-related functions.
import os.path
def createWordlist(wordlist): 
    infile = open( wordlist, "r")
    count = 0
    keywordsfound = list()
    line = infile.readline()
    while line:
        word = line.strip()
        if len(word) == 5 and word[-1] != 's' and len(word) == len(set(word)):
                    count += 1
                    keywordsfound.append(word)
        line = infile.readline()
    return(keywordsfound, count)


def containsAll(wordlist, include):
    count = 0
    mylist = []
    for word in wordlist:
       for letter in include:
          if letter in word:
             count += 1
             if count == len(include):
                mylist.append(word)
    return set(mylist)

def containsNone(wordlist, exclude):
    count = 0
    mylist = []
    for word in wordlist:
        contain = False
        for letter in exclude:
            if letter in word:
                contain = True
        if not contain:
            mylist.append(word)
    return set(mylist)


def containsAtPositions(wordlist, posInfo):
    mylist = []
    for word in wordlist:
        if word[0] == 'a' and word[4] == 'y':
            mylist.append(word)
        if word[0] == 'a' and word[1] == 'b':
            mylist.append(word)
    return set(mylist)

def getPossibleWords(wordlist, posInfo, include, exclude):
    s1 = containsAtPositions(wordlist, posInfo)
    s2 = containsAll(wordlist, include)
    s3 = containsNone(wordlist, exclue)

    s12 = s1.intersection(s2)
    return s12.intersection(s3)


wordlist, count = createWordlist( 'wordlist.py' )
for i in range(10):
    print(wordlist[i], end = " ")
print()

setABC = containsAll(wordlist, 'abc')
print(setABC)

someWords = containsNone( wordlist, 'abcdefghijklmn' ) 
print(someWords)

someMoreWords = containsNone( wordlist, 'abcdefghijklmnopqrstuvw' )
print(someMoreWords)

posDict = {'a':0, 'y':4}
posWords = containsAtPositions( wordlist, posDict )
print(posWords)
