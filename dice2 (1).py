#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# dice.py
# Roger Sundh
# 2015-01-26

#Generera ett slumpmässigt heltal (tärning) mellan 1 och 6

#Imports -------------------
import random

#Functions -----------------
#Skapa en etta
def printOne():
    print('     ')
    print('  *  ')
    print('     ')

#Skapa en tvåa
def printTwo():
    print('*    ')
    print('     ')
    print('    *')

#Skapa en trea
def printThree():
    print('*    ')
    print('  *  ')
    print('    *')

#Skapa en fyra
def printFour():
    print('*   *')
    print('     ')
    print('*   *')

#Skapa en femma
def printFive():
    print('*   *')
    print('  * ')
    print('*   *')

#Skapa en sexa
def printSix():
    print('*   *')
    print('*   *')
    print('*   *')

#Main program ----------------
die1 = random.randint(1,6)
print(die1)

if (die1==1):
    printOne()
elif (die1==2):
    printTwo()
elif (die1==3):
    printThree()
elif (die1==4):
    printFour()
elif (die1==5):
    printFive()
elif (die1==6):
    printSix()

