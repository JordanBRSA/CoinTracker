import requests

BASE_URL = "https://api.coingecko.com/api/v3"


def get_crypto_price(crypto,currency):

    URL_API = f"{BASE_URL}/simple/price"
    params = {
        "ids": crypto,
        "vs_currencies": currency
    }
    r = requests.get(URL_API, params=params)

    # print(URL_API)
    # print(r)
    # print(r.status_code)
    # print(r.json())


    return r.json()[crypto][currency]





