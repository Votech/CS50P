def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check that first two chars are letters
    first_two = s[0:2]
    if first_two.isalpha() is False:
        return False
    # Check that is two to six chars long
    if len(s) < 2 or len(s) > 6:
        return False
    # Check that all number are at the end and don't start with zero
    index_of_first_number = None
    for index, char in enumerate(s):
        if char.isnumeric():
            index_of_first_number = index
            break
    if index_of_first_number:
        ending_numbers = s[index_of_first_number:]
        if ending_numbers[0] == "0":
            return False
        if not ending_numbers.isnumeric():
            return False
    # Check that no periods, spaces, or punctuation marks
    for char in s:
        if not char.isalpha() and not char.isnumeric():
            return False
    return True


if __name__ == "__main__":
    main()
