months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def print_date(year, month, day):
    print(f"{int(year)}-{int(month):02}-{int(day):02}")


def main():
    while True:
        date = input("Date: ")
        try:
            month, day, year = date.split("/")
            if int(month) > 12 or int(day) > 31:
                continue
            print_date(year, month, day)
            break
        except ValueError:
            try:
                month, day, year = date.split(" ")
                for i in range(len(months)):
                    if month == months[i]:
                        month = i + 1
                if "," not in day:
                    continue
                day = day.replace(",", "")
                if int(month) > 12 or int(day) > 31:
                    continue
                print_date(year, month, day)
                break
            except ValueError:
                continue


main()
