import sys


def is_argv_valid(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    if argv[1][-3:] != ".py":
        sys.exit("Not a Python file")


def get_number_of_lines(file):
    lines = []
    for line in file:
        is_blank = len(line.strip()) == 0
        is_comment = line.strip().startswith("#")
        if not is_blank and not is_comment:
            lines.append(line)
    return len(lines)


def main():
    is_argv_valid(sys.argv)
    file_path = sys.argv[1]
    try:
        file = open(file_path)
        print(get_number_of_lines(file))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
