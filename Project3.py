# File: Project3.py
# Student: Danielle Balque
# UT EID: dsb2643
# Course Name: CS303E
# 
# Date: 11/30/22
# Description of Program: This program implements a substitution cipher class to encrypt and decrypt a file specified by the user.

import random

LETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey( key ):
     key = key.lower()
     return ( len(key) == 26 and all( [ ch in key for ch in LETTERS ] ) )

def makeRandomKey():
     lst = list( LETTERS )   
     random.shuffle( lst )    
     return ''.join( lst )

class SubstitutionCipher:
     def __init__ ( self, key = makeRandomKey() ):
         self.__key = key


     def getKey( self ):
         return self.__key

     def setKey( self, newKey ):
         self.__key = newKey
         

     def encryptFile( self, inFile, outFile ):
          dic = {}
          text = ""
          for i in range(len(LETTERS)):
               dic[LETTERS[i]] = self.__key[i]
          in_file = open( inFile, "r" )
          out_file = open( outFile, "w" )
          lines = in_file.readlines()
          for line in lines:
               for ch in line:
                    if ch.isalpha():
                         if ch.isupper():
                              ch = ch.lower()
                              enc = dic[ch].upper()
                         else:
                              enc = dic[ch]
                    else:
                         enc = ch

               text += enc
          out_file.write(text)

     def decryptFile( self, inFile, outFile ):
          dic = {}
          text = ""
          for i in range(len(LETTERS)):
               dic[LETTERS[i]] = self.__key[i]
          in_file = open( inFile, "r" )
          out_file = open( outFile, "w" )
          lines = in_file.readlines()
          for line in lines:
               for ch in line:
                    if ch.isalpha():
                         if ch.isupper():
                              ch = ch.lower()
                              decr = dic[ch].upper()
                         else:
                              decr = dic[ch]
                    else:
                         decr = ch

               text += decr
          out_file.write(text)
       
def main():
    input_=""
    obj = SubstitutionCipher()
    while(input_ != "quit"):
          print()
          input_ = input("Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ").lower()
          if(input_ == "getkey"):
               print("  Current cipher key:", obj.getKey())

          elif(input_ == "changekey" ):
               key = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
               while(key != "quit"):
                    if(key == "random"):
                         obj.setKey( makeRandomKey() )
                         print("    New cipher key: ", obj.getKey())
                         break
                    elif(isLegalKey(key)):
                              obj.setKey(key)
                              print("    New cipher key: ", obj.getKey())
                              break
                    else:
                         print("    Illegal key entered. Try again!")

                    key = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
          elif( input_ == "encryptfile" ):
               inFilename = input("  Enter a filename: ").lower()
               extension = "-Enc"

               if inFilename != "gettysburg-address.txt":
                    print("File does not exist")

               else:
                    if inFilename.endswith(".txt"):
                         
                         outFilename = inFilename[:-4] + extension + ".txt"

                    else:

                         outFilename = inFilename + extension

                    print("The encrypt output filename is", outFilename)
                    obj.encryptFile(inFilename, outFilename)

          elif( input_ == "decryptfile" ):
               inFilename = input("  Enter a filename: ")
               extension = "-Dec"

               if inFilename != "gettysburg-address-Enc.txt":
                    print("File does not exist")

               else:

                    if inFilename.endswith(".txt"):

                         outFilename = inFilename[:-4] + extension + ".txt"

                    else:

                         outFilename = inFilename + extension

                    print("The decrypt output filename is", outFilename)
                    obj.decryptFile(inFilename, outFilename)

                    

          elif( input_ == "quit" ):
               print("Thanks for visiting!") 
               print()
          else:
               print("  Command not recognized. Try again!")

main()
          
