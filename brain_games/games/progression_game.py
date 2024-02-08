import random


INSTRUCTION = 'What number is missing in the progression?'
PROGR_LENGTH_MIN = 5
PROGR_LENGTH_MAX = 10


def generate_round() -> tuple:
    while True:
        start, step = (random.randint(1, 100), random.randint(1, 10))
        end = start + random.randint(1, 100)
        progression = list(range(start, end + 1, step))
        if 5 <= len(progression) <= 10:
            missed_index = random.randint(0, len(progression) - 1)
            missed_num = progression[missed_index]
            progression[missed_index] = '..'
            progression_string = ' '.join(map(str, progression))
            return progression_string, str(missed_num)
