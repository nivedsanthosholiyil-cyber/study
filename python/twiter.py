def main():
    word = input("inpu:")
    print("output:",shorten(word))


def shorten(word):
    result = ""

    for letter in word:
        
         if letter not in "AEIOUaeiou":
            result = result + letter
    return result

    


if __name__ == "__main__":
    main()zz