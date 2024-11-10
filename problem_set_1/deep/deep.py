def main():
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything?"
    )
    answer_formatted = answer.strip().lower()

    match answer_formatted:
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "forty two":
            print("Yes")
        case _:
            print("No")


main()
