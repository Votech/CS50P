from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet_fonts = figlet.getFonts()
argv_len = len(sys.argv)


def main():
    if argv_len == 1:
        random_font = random.choice(figlet_fonts)
        figlet.setFont(font=random_font)
    elif argv_len == 3:
        is_first_arg_ok = sys.argv[1] in ["-f", "--font"]
        is_second_arg_ok = sys.argv[2] in figlet_fonts
        if not is_first_arg_ok or not is_second_arg_ok:
            sys.exit("Invalid usage")
        else:
            figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    text = input()
    print(figlet.renderText(text))


main()
