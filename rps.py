
import random

#Global variable
option = ['rock','paper','scissor']

if __name__ == "__main__":
    game_on = True

    while game_on:
        print('Choose one of the three options:')
        c = input('''
            [1] - Rock
            [2] - Paper
            [3] - Scissor
        \n''')
        cpu_option = option[random.randint(0,2)]
        print(cpu_option)
        if c == 'y':
            game_on = True
        elif c == 'n':
            game_on = False
        else:
            print('invalid input')
    
    print('bye bye')
        
