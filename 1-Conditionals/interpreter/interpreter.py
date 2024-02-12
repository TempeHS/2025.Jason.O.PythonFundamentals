def main():
    equation = input("Enter your equation: ")
    (
        x,
        y,
        z,
    ) = equation.split(" ")

    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    else:
        print(float(x) / float(z))


main()
