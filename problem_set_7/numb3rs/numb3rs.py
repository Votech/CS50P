import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if match:
        for group in match.groups():
            if int(group) > 255 or int(group) < 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
