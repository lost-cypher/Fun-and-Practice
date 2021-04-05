# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:07:32 2021
Just something to play with.
Program will run in the console.
You get to pick what the hightest possible Number is. 
Then you try to guess which number the computer picked between 1 and your number.
@author: lost-cypher
"""

import random as r

def logo_printer():
    print('''            ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              ""
              ''')
def check_input(msg):
    #Check if User entered an Integer or not. Loops until he does.
    while True:
        try:
            my_input = int(input(msg))
            return my_input
        except:
            print('Please try again')
            continue


def keep_playing():
    #Check if User wants to keep playing. Only accept 'y' or 'n'.
        while True:
            play_more = input('Do you want to continue Playing? y/n')
            if play_more.lower() == 'y':
                game()
                return
            elif play_more.lower() == 'n':
                return
            else:
                print('only y or n')
                continue
            

def game():
    logo_printer()
    #ask for Upper Limit of possible Numbers
    num = check_input('Enter the maximum possible Number: ')
        
    #create actual random number
    num = r.randint(1,num)
    
    print('I picked a number')
    guess = check_input('Guess it: ')
    
    #gameloop - keeps you guessing until you finish
    while True:
        if guess < num:
            guess = check_input(f'Higher than {guess} \n')
        elif guess > num:
            guess = check_input(f'Lower than {guess} \n')
        elif guess == num:
            print('Congrats. You found my number.')
            #do you want to keep playing?
            keep_playing()
            #if not bye 
            break


game()
