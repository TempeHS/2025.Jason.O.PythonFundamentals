from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    randomF = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    randomF = False
else:
    print("Invalid Usage")
    sys.exit()


figlet.getFonts()


if randomF == False:
    try:
        figlet.setFont(font=sys.argv[2])

    except:
        print("Invalid Usage")
        sys.exit()
else:
    font = random.choice(figlet.getFonts())

text = input("Text: ")

print(f"{figlet.renderText(text)}")
