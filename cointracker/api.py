import requests

def get_crypto_price(symbol: str, currency: str = "usd") -> float:
    """Récupère le prix d'une crypto via l'API CoinGecko."""
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": symbol, "vs_currencies": currency}

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception("Erreur lors de la requête à CoinGecko")

    data = response.json()
    if symbol not in data:
        raise ValueError(f"Crypto '{symbol}' introuvable sur CoinGecko")

    return data[symbol][currency]