import sys
from tabulate import tabulate


def is_argv_valid(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    if argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")


def get_table(file):
    lines = []
    for line in file:
        lines.append(line.rstrip().split(","))
    headers = lines[:1][0]
    table = lines[1:]
    return tabulate(table, headers, tablefmt="grid")


def main():
    is_argv_valid(sys.argv)
    file_path = sys.argv[1]
    try:
        with open(file_path) as file:
            print(get_table(file))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
