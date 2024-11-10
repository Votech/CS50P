def main():
    amount_due = 50
    change_owed = 0
    while amount_due > 0:
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            amount_due = amount_due - coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
            if amount_due < 0:
                change_owed = amount_due * -1
        else:
            print(f"Amount Due: {amount_due}")
    print(f"Change Owed: {change_owed}")


main()
