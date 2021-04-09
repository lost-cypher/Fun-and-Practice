# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:01:32 2021

@author: Sebastian
"""
import random as r
from IPython import get_ipython

#one deck of 52 cards
cards = [
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11,
             2,3,4,5,6,7,8,9,10,10,10,10,11
        ]
#save cards
backup = cards.copy()
#initialize empty hands
players_hand = []
dealers_hand = []

def clear():
    #need to clean up some console?
    get_ipython().magic('clear')
    
def sum_up(ar):
    #i can sum this up with one number
    s = 0
    for i in ar:
        s += i
    return s

def pick_and_delete():
    #what's mine is mine and you can't have it
    pick = r.choice(cards)
    cards.remove(pick)
    return pick

def chck_win(p,d):
    #so who won?
    if sum_up(p) == 21 or sum_up(d) > 21:
        print(f'Player wins: {p}, Dealer: {d}')
        print(p)
        return True
    elif sum_up(p) > 21 or sum_up(d) == 21:
        print(f'Dealer wins: {d}, Player: {p}')
        print(d)
        return True
    else: 
        return False

def show_down(p,d):
    #who has the bigger ... Number ;) ?
    if sum_up(p) > sum_up(d):
        return f'Player wins: {p}, Dealer: {d}'
    elif sum_up(p)< sum_up(d):
        return f'Dealer wins: {d}, Player: {p}'
    else:
        return 'Draw'


def dealers_turn(p,d):
    #do what you must
    if sum_up(d) >= 17:
        return 'done'
    else:
        d.append(pick_and_delete())
        #print(chck_win(p,d))
        if chck_win(p,d) == True:
            return 'win'
        else: 
            return 'next'

def chck_input(text, a, b):
    #no third options here just a or b!
    while True:
        pick = input(text)
        if pick.lower() == a.lower() or pick.lower() == b.lower():
            return pick

            
def players_turn(p,d):
    #just let me do my thing here
    take_card = chck_input('Would you like to take another card?','y','n')
    if take_card == 'y':
        p.append(pick_and_delete())
        #print(chck_win(p,d))
        if chck_win(p,d) == True:
            return 'win'
        else:
            return 'next'
    else:
        return 'done'

def setup(p,d):
    #we all start at the same line
    d.append(pick_and_delete())
    p.append(pick_and_delete())
    d.append(pick_and_delete())
    p.append(pick_and_delete())
    dealer_done = False
    if chck_win(p,d) == True:
        return 
    else:
        while True:
            print(f'Players Hand: {p}')
            print(f'Dealers Hand: {d[0]}')
            turn = dealers_turn(p,d)
            if turn == 'win':
                break
            elif turn == 'done':
                dealer_done = True

            turn = players_turn(p,d)
            if turn == 'win': 
                break
            elif turn == 'done' and dealer_done == True:
                print(show_down(p,d))
                break
            
def game_loop():
    #let the ratrace begin
    while chck_input('Would you like to play another round?','y','n') == 'y': 
        cards = backup.copy()
        clear()
        print(
'''
888     888                888       d8b                888      
888     888                888       Y8P                888      
888     888                888                          888      
88888b. 888 8888b.  .d8888b888  888 8888 8888b.  .d8888b888  888 
888 "88b888    "88bd88P"   888 .88P "888    "88bd88P"   888 .88P 
888  888888.d888888888     888888K   888.d888888888     888888K  
888 d88P888888  888Y88b.   888 "88b  888888  888Y88b.   888 "88b 
88888P" 888"Y888888 "Y8888P888  888  888"Y888888 "Y8888P888  888 
                                     888                         
                                    d88P                         
                                  888P"                          
''')
        players_hand = []
        dealers_hand = []
        setup(players_hand, dealers_hand)



game_loop()
