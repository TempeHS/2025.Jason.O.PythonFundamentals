import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            break
    except:
        pass

num = random.randint(1, lvl)

while True:
    try:
        g = int(input("Guess: "))
        if g < 1:
            pass
        elif num == g:
            print("Just Right!")
            break
        elif num > g:
            print("Too Small!")
            pass
        elif num < g:
            print("Too Large! ")
            pass
        else:
            pass
    except:
        pass
