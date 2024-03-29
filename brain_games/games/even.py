import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_round() -> tuple:
    num = random.randint(1, 100)
    if is_even(num):
        answer = "yes"
    else:
        answer = "no"
    return num, answer
