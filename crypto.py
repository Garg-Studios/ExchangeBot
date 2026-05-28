import requests
import sys

if len(sys.argv) > 1:
    ticker = sys.argv[1].upper()
else:
    print("ERROR")
    sys.exit(1)




clean_ticker = ticker.upper().strip()

api_ticker = "XBT" if clean_ticker == "BTC" else clean_ticker
url = f"https://api.kraken.com/0/public/Ticker?pair={api_ticker}USD"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()

        if json_data.get('error'):
            print(f"Ticker '{clean_ticker}' not found on Kraken.")

        result = json_data['result']
        exact_pair_key = list(result.keys())[0]
        price = float(result[exact_pair_key]['c'][0])

        print(f"The price of {clean_ticker} is ${price:,.2f}")
except ValueError:
    print("Value Error, please contact developer with !help")
except Exception as e:
    print(f"Python Error: {e}, please contact developer with !help")
