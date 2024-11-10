def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    g = greeting.lower().strip()
    is_g_hello = g.startswith("hello")
    is_g_h = g.startswith("h")

    if is_g_hello:
        return "$0"
    elif is_g_h:
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
