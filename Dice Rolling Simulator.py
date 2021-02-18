import random

def roller():
    return random.randint(1,7)

while True:
    roll = input("Roll the dice? (Y/N) ")
    if roll.lower() == "y":
        print(roller())
    else:
        break