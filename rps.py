
import random

# Global variable
option = ['rock','paper','scissor']

# Function to let user enter the option
# 1 is Rock
# 2 is Paper
# 3 is Scissor
# if the user Try to enter a string in the input, the program will say "Data entered not valid, please enter a valid option"
# and if the user enter a number higher than 3 or lower than 1, the program will print "Enter a number between 1 and 3"
# then it will return to this function 
def data_input():
    while True:
        try:
            player = int(input('''
                [1] - Rock
                [2] - Paper
                [3] - Scissor
            \n'''))
            return player
        except ValueError:
            print('Data entered not valid, please enter a valid option')

# this function is to avoid repeating the same print
def result(win,cpu_option):
    if win:
        print('You win! The CPU choose', cpu_option)
    else:
        print('You lose! The CPU choose', cpu_option)


# Main function
if __name__ == "__main__":
    game_on = True
    cnt = [0,0]
    player = 0
    while game_on:
        print('Choose one of the three options:')

        while player > 3 or player <1:
            player = data_input()
            if player > 3 or player <1:
                print('Enter a number between 1 and 3')
            
        if player <= 3 and player > 0:
            player -= 1
        player_option = option[player]
        cpu_option = option[random.randint(0,2)]
        
        if player_option == cpu_option:
            print('Draw')
        elif player_option == 'rock':
            if cpu_option == 'scissor':
                win = True
                result(win,cpu_option)
            elif cpu_option == 'paper':
                win = False
                result(win,cpu_option)
        elif player_option == 'paper':
            if cpu_option == 'rock':
                win = True
                result(win,cpu_option)
            elif cpu_option == 'scissor':
                win = False
                result(win,cpu_option)        
        elif player_option == 'scissor':
            if cpu_option == 'paper':
                win = True
                result(win,cpu_option)
            elif cpu_option == 'rock':
                win = False
                result(win,cpu_option)

        stay = input('Wanna continue? (y/n) \n')
        if stay == 'y':
            game_on = True
            player = 0
        elif stay == 'n':
            game_on = False
        else:
            print('invalid input')
    
    print('bye bye')
        
