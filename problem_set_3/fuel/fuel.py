def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x_num = int(x)
            y_num = int(y)
            if x_num > y_num or y_num == 0:
                continue
            if not x.isdigit() or not y.isdigit():
                continue
            tank_full_in = round(x_num / y_num * 100)
            if tank_full_in >= 99:
                print("F")
                break
            elif tank_full_in <= 1:
                print("E")
                break
            else:
                print(f"{tank_full_in}%")
                break
        except ValueError:
            pass
        except ZeroDivisionError:
            break


main()
