def main():
    convert()


def convert():
    new = face.replace(":)", "🙂").replace(":(", "🙁")
    print(new)


face = input("Make a happy or sad face. ")
main()
