import inflect

p = inflect.engine()

names = []

while True:
    try:
        n = input("Name: ")
        names.append(n)

    except EOFError:
        print()
        break

output = p.join(names)
print("Adieu, adieu, to " + output)
