def main():
    greeting = input("Greetings:")
    print (value(greeting))


def value(greeting):
    greeting = greeting.lower()

    if greeting.startwith("hello"):
        return 0
    elif greeting.startwith("h"):
        return 20
    else :
        return 1000


if __name__ == "__main__":
    main()