import sys
import requests
import math

symbol = ""

if len(symbol) < 1 and len(symbol) > 5:
    print("Error: Symbols should be 1-5 characters")
    sys.exit(1)

if len(sys.argv) > 1:
    symbol = sys.argv[1].upper()
    print(f"Recieved: {symbol}")
else:
    print("ERROR")
    sys.exit(1)

url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers)
    data = response.json()

    result = data['chart']['result']
    if result is None:
        print("ERROR")
        sys.exit(1)
    else:
        meta = data['chart']['result'][0]['meta']
        price = meta['regularMarketPrice']
        currency = meta['currency']
        companyname = data['chart']['result'][0]['meta']['longName']
        print(f"{companyname} ({symbol}) Current Price: {price} {currency}")
        stockexchange = data['chart']['result'][0]['meta']['fullExchangeName']
        oneyearlow = data['chart']['result'][0]['meta']['fiftyTwoWeekLow']
        oneyearhigh = data['chart']['result'][0]['meta']['fiftyTwoWeekHigh']
        prev_close = data['chart']['result'][0]['meta']['previousClose']
        dollar_change = price - prev_close
        percent_change = (dollar_change / prev_close) * 100
        print(f"Exchange: {stockexchange}")
        print(f"52 Week Range: {oneyearlow}-{oneyearhigh}")
        print(f"1D: {round(dollar_change, 5)} USD ({round(percent_change, 5)}%) ")


except Exception as e:
    print(f"Failed to get data: {e}")