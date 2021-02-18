import random

a = int(input("Enter the limit of small number: "))
b = int(input("Enter the limit of big number: "))
number = random.randint(a, b)

while True:
    guess = int(input("Enter the guess: "))
    if guess == number:
        print(f"You guessed correct number was {guess}")
        new_game = input("Do you want to new game? (Y/N): ")
        if new_game.lower() == "y":
            a = int(input("Enter the limit of small number: "))
            b = int(input("Enter the limit of big number: "))
            number = random.randint(a, b)
            continue
        else:
            break
    else:
        if guess > number:
            print("Smaller")
        else:
            print("bigger")
