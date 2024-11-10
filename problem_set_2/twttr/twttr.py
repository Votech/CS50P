def main():
    input_word = input("Input: ")
    output_list = []
    for char in input_word:
        input_char = char
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            output_list.append(input_char)

    output = "".join(output_list)
    print(f"Output: {output}")


main()
