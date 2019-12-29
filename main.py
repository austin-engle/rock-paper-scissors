from random import randint
from time import sleep
from os import system

"""
    This is a rock-paper-scissors game that will be played between you and a bot with a random selection each time. First player to hit 3 wins (best of 5)
"""

p1_counter = 0
p2_counter = 0

t = {
    "1" : "Rock",
    "2" : "Paper",
    "3" : "Scissors"
}

while p1_counter < 3 and p2_counter < 3:

    system('clear')

    print('Score')
    print(f' {p1_counter}:{p2_counter}\n')

    num = input("Pick one of the following: 1: Rock, 2: Paper, 3: Scissors:\n")

    if num == '1' or num == '2' or num == '3':

        p1 = t[num]

        computer = t[str(randint(1,3))]

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
    else:
        continue

if p1_counter == 3:
    print(f'Congratulations, You Win: {p1_counter}:{p2_counter}')
else:
    print(f'You Lose: {p1_counter}:{p2_counter}')