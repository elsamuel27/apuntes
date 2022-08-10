import random


def ask_username():
    return print(input("Enter your name: "))

def roll_dice(num):
    return random.randint(1, num)