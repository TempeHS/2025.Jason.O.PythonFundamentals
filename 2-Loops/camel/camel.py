def main():
    camel = input("What's your name? ")
    for letter in camel:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")


main()
