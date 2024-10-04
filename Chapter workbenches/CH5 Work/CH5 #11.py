import random


def test():
    for question_number in range(1, 6):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        

        print(f"Question {question_number}")
        print(f"{num1} + {num2} = _____")


test()
