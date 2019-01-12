
import random

#Global variable
option = ['rock','paper','scissor']

if __name__ == "__main__":
    game_on = True
    cnt = [0,0]
    while game_on:
        print('Choose one of the three options:')
        player = int(input('''
            [1] - Rock
            [2] - Paper
            [3] - Scissor
        \n'''))
#        if player != 1 or player != 2 or player != 3:
#            print('Please insert a valid option')
        if player <= 3 and player > 0:
            player -= 1
        player_option = option[player]
        cpu_option = option[random.randint(0,2)]
        
        if player_option == cpu_option:
            print('Draw')
        elif player_option == 'rock':
            if cpu_option == 'scissor':
                print('You win! The CPU choose', cpu_option , player_option)
            elif cpu_option == 'paper':
                print('You lose! The CPU choose', cpu_option)
        elif player_option == 'paper':
            if cpu_option == 'rock':
                print('You win! The CPU choose', cpu_option)
            elif cpu_option == 'scissor':
                print('You lose! The CPU choose', cpu_option)        
        elif player_option == 'scissor':
            if cpu_option == 'paper':
                print('You win! The CPU choose', cpu_option)
            elif cpu_option == 'rock':
                print('You lose! The CPU choose', cpu_option)

        stay = input('Wanna continue? (y/n) \n')
        if stay == 'y':
            game_on = True
        elif stay == 'n':
            game_on = False
        else:
            print('invalid input')
    
    print('bye bye')
        
