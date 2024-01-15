import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

available_fonts = figlet.getFonts()

def output_font(font):
    user_input = input("Input: ")
    figlet.setFont(font=font)
    print("Output: \n",figlet.renderText(user_input), sep="")



if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    elif sys.argv[2] not in available_fonts:
        sys.exit("Invalid usage")
    else:
        output_font(sys.argv[2])

elif len(sys.argv) == 1:
    chosen = random.choice(available_fonts)
    output_font(chosen)

else:
    sys.exit("Invalid usage")

