import random

number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess<number:
        print("Increase your number.")
    elif guess>number:
        print("Decrease your number.")
    
    else:
        print("Congrats! You found it.")
        break