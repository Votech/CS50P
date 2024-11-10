def main():
    greeting = input("Greeting: ").lower().strip()
    is_greeting_hello = greeting.startswith("hello")
    is_greeting_h = greeting.startswith("h")

    if is_greeting_hello:
        print("$0")
    elif is_greeting_h:
        print("$20")
    else:
        print("$100")


main()
