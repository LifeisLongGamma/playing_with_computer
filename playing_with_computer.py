import random

def computer_attempt(number, number1):
    min = number
    max = number1
    hint = ''
    while hint != 'yes':
        if min != max:
            hidden_number = random.randint(min, max)
        else:
            hidden_number = max
        hint = input(f'My guess is {hidden_number}. Am I correct? If so input \'yes\'. \
Otherwise, tell me if it is high (H) or low (L):').lower()
        if hint == 'yes':
            print(f'How smart you are! You have guessed correctly. The hidden number is {hidden_number}.')
        elif hint == 'h':
            max = hidden_number - 1
        elif hint == 'l':
            min = hidden_number + 1

user_input = int(input('Please input your min number in a numeric form: '))
user_input1 = int(input('Please input your max number in a numeric form \
so that within a range of two given numbers I would hide a number for you to guess: '))

computer_attempt(user_input, user_input1)
