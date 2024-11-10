def convert(str):
    str_converted = str.replace(":(", "🙁").replace(":)", "🙂")
    return str_converted


def main():
    text = input()
    text_converted = convert(text)
    print(text_converted)


main()
