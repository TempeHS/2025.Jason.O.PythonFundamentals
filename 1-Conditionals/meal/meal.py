def main():
    time = input("What time is it? ")
    time = convert(time)


def convert(time):
    (
        x,
        y,
    ) = time.split(":")
    h = x
    m = y

    if 7 <= float(h) <= 8:
        print("Breakfast time")
    elif 12 <= float(h) <= 13:
        print("Lunch time")
    elif 18 <= float(h) <= 19:
        print("Dinner time")


main()
