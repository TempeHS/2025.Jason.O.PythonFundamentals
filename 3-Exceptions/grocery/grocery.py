cart = {}

while True:
    try:
        item = input("Item: ").upper()
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1

    except EOFError:
        for key in sorted(cart.keys()):
            print(cart[key], key)
        break
