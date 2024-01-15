import json
import requests
import sys

def check_type(value):
    try:
        float_value = float(value)
        return isinstance(float_value, (int, float))
    except ValueError:
        return False

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif not check_type(sys.argv[1]):
    sys.exit("Command-line argument is not a number")
else:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        usd_rate_str = data['bpi']['USD']['rate']

        usd_rate = float(usd_rate_str.replace(",", ""))
        
        amount = usd_rate * float(sys.argv[1])

        print(f"${amount:,.4f}")

    except requests.RequestException:
        sys.exit()
