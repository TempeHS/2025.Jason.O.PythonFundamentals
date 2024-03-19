import sys
import csv
from tabulate import tabulate


def main():
    check_CLA()
    table = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


def check_CLA():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
