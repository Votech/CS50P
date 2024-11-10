import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    r_time = "(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + r_time + " to " + r_time + "$", s)
    if match:
        time_from = serialize_time(match.group(1), match.group(2), match.group(3))
        time_to = serialize_time(match.group(4), match.group(5), match.group(6))
        return f"{time_from} to {time_to}"
    else:
        raise ValueError


def serialize_time(h, m, day_time):
    new_h = None
    new_m = None
    if day_time == "AM":
        if h == "12":
            new_h = "00"
        else:
            new_h = f"{int(h):02}"
    else:
        if h == "12":
            new_h = "12"
        else:
            new_h = f"{int(h) + 12}"

    if m == None:
        new_m = "00"
    else:
        new_m = f"{int(m):02}"

    return f"{new_h}:{new_m}"


if __name__ == "__main__":
    main()
