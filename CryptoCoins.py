
import requests
import CryptoApiKey


def trading(wallet):
# Got this information from coinmarketcap 
    headers = {"X-CMC_PRO_API_KEY": CryptoApiKey.apiKey,
          "Accepts": "application/json" 
    }

# made a dictionary for that will be able to take the first five crypto coins from coinmarketCap list
    params = {
    "start" : "1",
    "limit" : "100",
    "convert" : "USD"
  }

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

#Stored jason object from the request
# this information is from https://jsonformatter.curiousconcept.com/#
    json = requests.get(url, params=params, headers=headers,).json()
    crypto = json["data"]
    
#prints out the symbol and price of the crypto and the converted currency which is USD
# the Crypto price should update every few seconds
#while loops that allows the user to buy or sell the cryptocurrency 
    while True:
        print("\nTrading Options")
        print("1. Buy")
        print("2. Sell")
        print("3. Exit Trading")

        choice2 = int(input("Enter your choice (1 to Buy, 2 to Sell, 3 to Exit): "))

        if choice2 == 1 or choice2 == 2:
            coin = input("Enter the coin symbol: ").upper()
            amount = float(input(f"Enter the amount of {coin} to {'buy' if choice2 == 1 else 'sell'}: "))
            # item is the crypto list on coin market it access the price of the cryptocurrency
            price = next((item['quote']['USD']['price'] for item in crypto if item['symbol'] == coin), None)

            if price is None:
                print("Invalid coin symbol, please try again.")
                continue

            if choice2 == 1:
                wallet.buy(coin, amount, price)
            elif choice2 == 2:
                wallet.sell(coin, amount, price)

        elif choice2 == 3:
            print("Exiting Trading...")
            break

        else:
            print("Invalid choice, please try again")


        
    
        
