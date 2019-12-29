from random import randint
from time import sleep
from os import system

"""
    This is a rock-paper-scissors game that will be played between you and a bot with a random selection each time. First player to hit 3 wins (best of 5)
"""

p1_counter = 0
p2_counter = 0

t = ['Rock','Paper','Scissors']

while p1_counter < 3 and p2_counter < 3:

    system('clear')

    print('Score')
    print(f' {p1_counter}:{p2_counter}\n')

    p1 = input("Type one of the following: Rock, Paper, Scissors:\n").capitalize()

    computer = t[randint(0,2)]

    print(f'\nPlayer 1: {p1} \nComputer: {computer}')
    sleep(0.5)

    if p1 == computer:
        print('\nTie!\n')

    elif p1 == 'Rock':
        if computer == 'Scissors':
            print(f'\nYou win: {p1} beats {computer}\n')
            p1_counter+=1
            
        else:
            print(f'\nYou lose: {p1} loses to {computer}\n')
            p2_counter+=1
    
    elif p1 == 'Paper':
        if computer == 'Rock':
            print(f'\nYou win: {p1} beats {computer}\n')
            p1_counter+=1
            
        else:
            print(f'\nYou lose: {p1} loses to {computer}\n')
            p2_counter+=1

    elif p1 == 'Scissors':
        if computer == 'Paper':
            print(f'\nYou win: {p1} beats {computer}\n')
            p1_counter+=1
            
        else:
            print(f'\nYou lose: {p1} loses to {computer}\n')
            p2_counter+=1

    else:
        print('\nInvalid Input\n')
    
    sleep(3)

if p1_counter == 3:
    print(f'Congratulations, You Win: {p1_counter}:{p2_counter}')
else:
    print(f'You Lose: {p1_counter}:{p2_counter}')