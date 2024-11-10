import inflect


def main():
    p = inflect.engine()

    names = []

    print("Enter names, one per line (press Ctrl-D to finish):")
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break

    farewell = f"Adieu, adieu, to {p.join(names)}"
    print(farewell)


if __name__ == "__main__":
    main()
