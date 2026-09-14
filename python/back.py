def main():
    greeting = input("Greetings:")
    print (value(greeting))


def value(greeting):
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else :
        return 1000


if __name__ == "__main__":
    main()