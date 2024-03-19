import sys
import csv


def main():
    check_CLA()
    output = []
    try:
        with open("sys.argv[1]", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_name = row["name"].splt(",")
                output.append(
                    {
                        "name": split_name[1].lstrip(),
                        "last": split_name[0],
                        "house": row["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    with open("sys.argv[2]") as file:
        writer = csv.DictWriterwriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )


def check_CLA():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
