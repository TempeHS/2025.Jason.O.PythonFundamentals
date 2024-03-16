import csv

name = input("What's your name? ")
home = input("Where do you live? ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
