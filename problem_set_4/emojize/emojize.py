import emoji


def main():
    input_str = input()
    print(emoji.emojize(input_str, language="alias"))


main()
