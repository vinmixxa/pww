import random

def guess_numbers(a,b):
    guess_number = 0
    comp_number = random.randint(a,b)
    while guess_number != comp_number:
        guess_number = int(input("введите число "))

        if guess_number < comp_number:
            print('Загаданное число больше')
        elif guess_number > comp_number:
            print('Загаданное число меньше')
        else:
            print('Вы угадали!')

guess_numbers(int(input("Введите 1 предел ")),int(input("Введите 2 предел ")))