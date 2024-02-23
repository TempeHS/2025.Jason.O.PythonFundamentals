menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

cost = 0

while True:
    try:
        item = input("What will you be eating? ").title()
        if item in menu:
            cost += menu[item]
            print("Your total is: $", end="")
            print("{:.2f}".format(cost))

    except EOFError:
        print()
        break
