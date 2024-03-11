import random


def main():
    lvl = get_level()
    score = game(lvl)
    print("Score: ", score)


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl <= 3 and lvl >= 1:
                break
        except:
            pass
    return lvl


def generate_integer(lvl):
    if lvl == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif lvl == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


def round(x, y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False


def game(lvl):
    cround = 1
    score = 0
    while cround <= 10:
        x, y = generate_integer(lvl)
        response = round(x, y)
        if response == True:
            score += 1
        cround += 1
    return score


if __name__ == "__main__":
    main()
