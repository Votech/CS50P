def main():
    camel_case = input("camelCase: ")
    snake_case_list = []
    for char in camel_case:
        camel_case_char = char
        if char.isupper():
            camel_case_char = f"_{char.lower()}"

        snake_case_list.append(camel_case_char)

    snake_case = "".join(snake_case_list)
    print("snake_case: ", snake_case)


main()
