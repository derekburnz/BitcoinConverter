import requests
#https://github.com/icecloak/A3.git

# This scripts is getting data from CoinDesk API

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def showUsd():
    """
    This function sends GET request to CoinDesk API and show Bitcoin's current price in USD.
    """
    response = requests.get(url) # sending request to url
    jsonResponse = response.json() # saving response as JSON
    time = jsonResponse["time"]["updated"] # getting time from response
    code = jsonResponse["bpi"]["USD"]["code"] # getting currency code from response
    rate = jsonResponse["bpi"]["USD"]["rate"] # getting price in USD from response.

    print(time,code,rate)

def showGbp():
    """
    This function sends GET request to CoinDesk API and show Bitcoin's current price in USD.
    """
    response = requests.get(url)  # sending request to url
    jsonResponse = response.json()  # saving response as JSON
    time = jsonResponse["time"]["updated"]  # getting time from response
    code = jsonResponse["bpi"]["GBP"]["code"]  # getting currency code from response
    rate = jsonResponse["bpi"]["GBP"]["rate"]  # getting price in GBP from response.
    #print all
    print(time, code, rate)
def showEuro():
    """
    This function sends GET request to CoinDesk API and show Bitcoin's current price in USD.
    """
    response = requests.get(url)  # sending request to url
    jsonResponse = response.json()  # saving response as JSON
    time = jsonResponse["time"]["updated"]  # getting time from response
    code = jsonResponse["bpi"]["EUR"]["code"]  # getting currency code from response
    rate = jsonResponse["bpi"]["EUR"]["rate"]  # getting price in EUR from response.
    # print all
    print(time, code, rate)
    pass
while True:
    try:
        print("1. Show Bitcoin Price in USD.")
        print("2. Show Bitcoin Price in GBP.")
        print("3. Show Bitcoin Price in EUR.")
        userInput = int(input("Please Enter Your Choice: "))
        if userInput == 1:
            showUsd()
            break
        elif userInput == 2:
            showGbp()
            break
        elif userInput == 3:
            showEuro()
            break
        else:
            print("Something Went Wrong, Please Try Again...")
            continue
    except:
        print("Something Went Wrong, Quitting...")
        break
