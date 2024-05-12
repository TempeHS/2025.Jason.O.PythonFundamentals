def main():
    ask()


def ask():
    print(" 1. First Menu: \n 2. Second Menu: \n 3. Third Menu: \n 4. Exit: \n")
    choice = int(input("Choose a menu option: "))
    while True:
        if choice != 4:
            pass
        else:
            print("Thankyou for using using TextMenu")
            return False


if __name__ == "__main__":
    main()
