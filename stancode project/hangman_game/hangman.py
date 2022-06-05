"""
File: hangman.py
Name:Jan Guo
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program lets user guess a dashed word by inputting one character each round. If the input is correct, show the
    updated word on console. User has N_TURNS chances to try and win this game.
    """
    # To define how many chances left
    num = N_TURNS
    # Randomly chooses a word
    answer = random_word()
    # Replace each index in the answer with "-"
    dashed = ''
    for i in range(len(answer)):
        ch = answer[i]
        if ch.isalpha():
            dashed += '-'
    print('The word looks like: ' + dashed)
    print('You have '+str(N_TURNS)+' guesses left.')
    # what temporary answer is
    temp_ans = dashed

    while num > 0:
        # Get user input
        input_ch = input('Your guess:')
        # let input letter is case-insensitive, the letter input becomes uppercase
        input_ch = input_ch.upper()
        if len(input_ch) == 1 and input_ch.isalpha():
            # Inputting more than 1 time correct letter in the answer will get the same result
            if input_ch in temp_ans:
                print('You are correct!')
                print('The word looks like: ' + temp_ans)
                print('You have ' + str(num)+' guesses left.')
            elif input_ch not in answer:
                num = num - 1
                print('There is no ' + input_ch + "'s" + ' in the world')
                if num > 0:
                    print('The word looks like: ' + temp_ans)
                    print('You have ' + str(num) + ' guesses left.')
                # Stops the game when there is no more chance to guess a new letter
                else:
                    print('You are completely hung :(')
                    print('The word was:' + answer)
                    break
            else:
                print('You are correct!')
                # if input matches the letter in the answer, replace the index of temporary answer with actual letter
                for i in range(len(answer)):
                    if answer[i] == input_ch:
                        temp_ans = temp_ans[:i] + answer[i] + temp_ans[i+1:]
                # Keep asking until the answer is guessed
                if temp_ans != answer:
                    print('The word looks like: ' + temp_ans)
                    print('You have ' + str(num)+' guesses left.')
                # Stops the game when all letters in the answer are guessed
                else:
                    print('You win!!')
                    print('The word was:' + answer)
                    break
        # If user input is illegal format, keep asking the user to input until the input is correct format
        else:
            print('illegal format.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
