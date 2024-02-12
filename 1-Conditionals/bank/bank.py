def main():
    greet = input("How would your greet someone? ")
    greet = greet.lower().lstrip(" ")
    if greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
