from random import randint

score = 0
total_tries = 5


for _ in range (total_tries):
    number1 = randint(1,10)
    number2 = randint(1,10)

    user_input = int(input(f"What is {number1} * {number2}?"))

    problem =  number1*number2

    if user_input == problem:
        print("Correct!")
        score +=1
    else:
        print (f"Your Answer is wrong! The correct answer is {problem}!")

print(f"\nYou got {score} out of {total_tries} correct!")