def main():
    time_input = input("What time is it? ")
    time = convert(time_input)

    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours_num = float(hours)
    minutes_num = float(minutes)
    converted_time = hours_num + (minutes_num / 60)
    return converted_time


if __name__ == "__main__":
    main()
