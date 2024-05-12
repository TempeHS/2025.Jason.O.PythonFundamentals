from datetime import date
import re
import sys
import inflect

p = inflect.engine


def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_bd(birth_date)
    except:
        sys.exit("Invalid Date")

    dob = date(int(year), int(month), int(day))
    dot = date.today()
    diff = dot - dob
    total_min = diff.days * 24 * 60
    output = p.number_to_words(total_min, andword="")
    print(output.capitalize() + "minutes")


def check_bd(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
