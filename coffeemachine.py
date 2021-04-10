# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:16:45 2021

@author: Sebastian

Welcome to my special virtual Coffee Maker

Pick between 
Coffee      -    2€
Latte       -    2.30€
Espresso    -    1.50€

Typing 'off' at any point will shut down the coffeemachine
Typing 'report' at any point will show you the currently available resources

Enjoy your hot beverage :D
"""
import sys

resources = {'water':1000,
             'milk':1000,
             'coffee':2000,
             'money':0
             }

drink_options = {'Coffee':{'water':200,'milk':0,'coffee':80,'money':2},
                 'Latte':{'water':100,'milk':100,'coffee':80,'money':2.30},
                 'Espresso':{'water':100,'milk':0,'coffee':120,'money':1.5}
                 }

#TODO: Prompt user by asking what would you like?
def choose_drinks(d):
    drinks = list(d)
    drink = chck_txt(input(f'What would you like? {drinks}'))
    if drink in drinks:
        return drink
    else:
        print(f'You may only choose from these {drinks}!')
        choose_drinks(d)
        
#TODO: Turn off the Coffee Machine by entering 'off' to the prompt
def chck_txt(txt):
    if txt == 'off':
        print('Machine shutting down...')
        sys.exit()
    elif txt == 'report':
        print_report()
    else:
        return txt
    
#TODO: Print Report when user enters 'report' into the prompt
def print_report():
    global recources
    r = resources
    print(f'''\n
          Water:    {r["water"]}ml
          Milk:     {r["milk"]}ml
          Coffee:   {r["coffee"]}g
          Money:    {r["money"]}€
          ''')
    loop()
#TODO: Check for sufficient resources
def chck_resources(d ,r):
    global drink_options
    needed_resources = drink_options[d]
    
    for key in r:
        if r[key] < needed_resources[key]:
            return key
    return True

#TODO: Process Coins
def take_coins():
    global resources
    coin_options = [.1,.2,.5,1,2]
    val = 0
    for i in coin_options:
        try:
            txt = chck_txt(input(f'How many pieces of {i} will you insert?'))
            if txt == '':
                val += 0
            else:
                val += i * int(txt)
        except:
            return take_coins()
    return val

#TODO: Check for successful transaction
def transact(t,d):
    global resources
    if t == True:
        print(f'you chose {d}. There are enough resources')
        for key in resources:
            resources[key] -= drink_options[d][key]
        print(f'Here is your {d}')
        print(f'You get {round(float(resources["money"]),2)} € back')
        resources['money'] = 0 
    else:
        print(f'Not enough {t}')
        if t == 'money':
            while resources['money'] < drink_options[d]['money']:
                take_coins()
            transact(t,d)
    
    
#TODO: Make Coffee
def loop():
    
    global resources
    
    while chck_txt(input('do you want another drink? y/n')) == 'y': 
        d = choose_drinks(drink_options)
        resources['money'] = take_coins()
        t = chck_resources(d, resources)
        transact(t,d)

loop()