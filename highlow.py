# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:15:53 2021

@author: Sebastian
"""

import highlow_data as d
import random as r


def compare_ab(a,b):
    if a > b:
        return 'a'
    else:
        return 'b'
    
def game(a,b):
    print(f'a {a["description"]} {a["name"]} from {a["country"]}')
    print('vs')
    print(f'b {b["description"]} {b["name"]} from {b["country"]}')
    user_in = input('who has more folloers? a or b?').lower()
    fact_check = compare_ab(a['follower_count'], b['follower_count'])
    if user_in == fact_check:
        return True
    else:
        return False

def loop_me():
    a = r.choice(d.data)
    b = r.choice(d.data)
    streak = 0
    while game(a,b) == True:
        streak += 1
        a = b
        b = r.choice(d.data)
    print(f'You won {streak} rounds in a row')


loop_me()
while input('do you want to keep playing? y/n') == 'y':
    loop_me()