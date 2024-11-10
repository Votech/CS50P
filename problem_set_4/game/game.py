import random
import sys


def main():
    level = None
    target = None
    guess = None

    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
            else:
                continue
        except ValueError:
            continue

    target = random.randint(0, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > target:
                print("Too large!")
            elif guess < target:
                print("Too small!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


if __name__ == "__main__":
    main()
