
import random
while True:
    try:
        level = int(input("level"))
        if level > 0:
             break
    except ValueError:
        pass

number = random.randint(1, level)

while True:
    try:
        guess= int(int(input))
        if guess < 1:
            continue

        if guess < number:
            print("number too low")
        elif guess > number:
            print("number too high")
        else:
            print("Just right!")
            break

    except ValueError:
        pass