import sys
import requests

currency = ""

'''if len(currency) < 1 and len(currency) > 5:
    print("Error: Symbols should be 1-5 characters")
    sys.exit(1)''' # error handling


if len(sys.argv) > 1:
    currency = sys.argv[1].upper()
    currency_amount = float(sys.argv[2])
    conversioncurrency = sys.argv[3].upper()
else:
    print("ERROR")
    sys.exit(1)

try:
    url = f"https://api.frankfurter.dev/v1/latest?base={currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data['rates']


        currencylist = ["EUR", "GBP", "JPY", "INR", "USD"]
        resultlist = []
        for x in range(len(currencylist)):
            if currency == currencylist[x]:
                resultlist.append(currency_amount)
            else:
                loopcurrency = currency_amount * rates[currencylist[x]]
                resultlist.append(loopcurrency)
        displayusercurrency = True
        if conversioncurrency != "GBP" and conversioncurrency != "USD" and conversioncurrency != "EUR" and conversioncurrency != "INR" and conversioncurrency != "JPY":
            usercurrency = currency_amount * rates[conversioncurrency.upper()]
            displayusercurrency = True
        else:
            displayusercurrency = False

# DISPLAY
        print(f"\nResults for {currency_amount:,.2f} {currency}")
        print(f"---------------------------")
        print(f"Euro (EUR):            {resultlist[0]:,.2f}")
        print(f"British Pound:       {resultlist[1]:,.2f}")
        print(f"Japanese Yen:       {resultlist[2]:,.2f}")
        print(f"Indian Rupee:        {resultlist[3]:,.2f}")
        print(f"American Dollar:  {resultlist[4]:,.2f}")
        if displayusercurrency:
            print(f"{conversioncurrency}:                         {usercurrency:,.2f}") #even spacing
        print(f"---------------------------")
        print(f"Rates updated on: {data['date']}")

    else:
        print("Error: Could not connect to the exchange server. This may also be caused by incorrect formatting of currency")

except ValueError:
    print("Value Error")
except Exception as e:
    print(f"Something went wrong: {e}")

