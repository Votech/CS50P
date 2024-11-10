def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")

    num_1 = float(x)
    num_2 = float(z)
    match y:
        case "+":
            print(num_1 + num_2)
        case "-":
            print(num_1 - num_2)
        case "*":
            print(num_1 * num_2)
        case "/":
            print(num_1 / num_2)


main()
