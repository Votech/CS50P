import sys
import csv


def is_argv_valid(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(argv) > 3:
        sys.exit("Too many command-line arguments")
    if argv[1][-4:] != ".csv" and argv[2][-4] != ".csv":
        sys.exit("Not a CSV file")


def get_formatted_rows(file):
    reader = csv.DictReader(file)
    rows = []
    for row in reader:
        last, first = row["name"].split(",")
        rows.append(
            {"first": first.strip(), "last": last.strip(), "house": row["house"]}
        )

    return rows


def write_to_file(rows, file_path):
    try:
        with open(file_path, "w") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    is_argv_valid(sys.argv)
    file_path = sys.argv[1]
    second_file_path = sys.argv[2]
    try:
        with open(file_path) as file:
            formatted_rows = get_formatted_rows(file)
            write_to_file(formatted_rows, second_file_path)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
