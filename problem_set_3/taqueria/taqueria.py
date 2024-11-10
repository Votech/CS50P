menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0
    while True:
        try:
            item = input("Item: ")
            price = menu[item.title()]
            total = total + price
            formatted_total = "{0:.2f}".format(total)
            print(f"${formatted_total}")
        except EOFError:
            break
        except KeyError:
            pass


main()
