grocery = {}


def print_grocery_list():
    sorted_grocery = dict(sorted(grocery.items()))
    for item in sorted_grocery:
        print(f"{sorted_grocery[item]} {item.upper()}")


def main():
    while True:
        try:
            item = input().lower()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            print_grocery_list()
            break


main()
