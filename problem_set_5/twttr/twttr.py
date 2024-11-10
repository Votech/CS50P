def main():
    input_word = input("Input: ")
    print(f"Output: {shorten(input_word)}")


def shorten(word):
    output_list = []
    for char in word:
        input_char = char
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            output_list.append(input_char)

    return "".join(output_list)


if __name__ == "__main__":
    main()
