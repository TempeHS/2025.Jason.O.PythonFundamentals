with open("openclose.txt", "r") as file:
    for line in file:
        num = int(line)
        new = num + 1

with open("openclose.txt", "w") as file:
    file.write(f"{new}")
