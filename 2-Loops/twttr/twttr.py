def main():
    word = input("Input: ")
    for letter in word:
        if not letter.lowr() in ["a", "e", "i", "o", "u"]:
            print(letter, end="")


main()
