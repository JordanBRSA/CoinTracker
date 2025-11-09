from plyer import notification

from .api import get_crypto_price


def setupPriceAlert(args):

    if args.alert and len(args.symbol) > 1:
        raise ValueError("Veuillez saisir une seule crypto pour mettre une alerte.")

    if args.alert:
        crypto = args.symbol[0]
        alert_value = args.alert
        currency = args.currency

        print(f"⚠️ Alerte mise en place pour {crypto} à {alert_value} {currency}")

        price = get_crypto_price(crypto, currency)

        if price >= alert_value:
            notification.notify(
                title=f"Alerte {crypto}",
                message=f"{crypto} a atteint {price} {currency} !",
                timeout=5
            )







def afficherCryptos(cryptos, currency):

    print("__________CoinTracker__________\n")
    res = {}

    for coin in cryptos:
        price = get_crypto_price(coin, currency)  # récupère le prix
        res[coin] = price                         # stocke dans le dictionnaire
        print(f"Valeur de {coin} : {price} {currency}")
        print("____________________\n")

    return res

