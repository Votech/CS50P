import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price")

    cost = num_bitcoins * bitcoin_price

    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
