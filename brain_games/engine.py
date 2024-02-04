import prompt
from brain_games.consts import AMOUNT_OF_ROUNDS


def run_game(get_question_and_answer: callable, instruction):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!'
          f'{instruction}')

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = get_question_and_answer()

        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer is {correct_answer}.\n"
                  f"Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')
