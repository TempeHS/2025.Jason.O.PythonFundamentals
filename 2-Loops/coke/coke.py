cost = 50
while cost > 0:
    pay = int(input("Insert coin: "))
    print("Amount Due: ", int(cost) - pay)
    cost = cost - pay

while cost < 0:
    print("Change Owed: ", -cost)
    break
