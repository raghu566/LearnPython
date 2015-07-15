__author__ = 'adamtalbot'

import random #package for random number generator

min = 1 #minimum number on dice
max = 6 #maximum number on dice

roll_again = input("Would you like to roll the dice?") #initial question

while roll_again == "Yes" or roll_again == "Y" or roll_again == "y" or roll_again == "Y": #if yes answer to question
    roll_number = int(input("How many dice would you like to roll?"))
    for i in range(0,roll_number):
        print(random.randint(min,max)) #spit out random numbers
    roll_again = input("Would you like to roll again?") 
