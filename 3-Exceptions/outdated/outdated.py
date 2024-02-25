month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        date = input("Date: ")
        m, d, y = date.split("/")
        if int(m) >= 1 and int(m) <= 12 and int(d) >= 1 and int(d) <= 31:
            break

        oldm, oldd, y = date.split(" ")
        for i in range(len(month)):
            if oldm == month[1]:
                m += 1

        day = oldd.replace(",", "")
        if int(m) >= 1 and int(m) <= 12 and int(d) >= 1 and int(d) <= 31:
            break

    except:
        print()
        pass

print(f"{y}-{int(m):02}-{int(d):02}")
