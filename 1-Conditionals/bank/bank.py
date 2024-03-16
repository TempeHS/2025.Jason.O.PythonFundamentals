def main():
    greet = input("How would your greet someone? ")
    greet = greet.lower().lstrip(" ")
    if greet.startswith("hello"):
        print("$100")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$0")


main()
