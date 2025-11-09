from cointracker.api import get_crypto_price
from plyer import notification
import argparse
import requests
from cointracker.utils import afficherCryptos,setupPriceAlert
import sys


def main():

    parser = argparse.ArgumentParser()                                      # Permet de pouvoir saisir des arguments dans le terminal
    parser.add_argument("symbol",nargs="*",default=["bitcoin"])  # 1er arguments -> symbol        # nargs = * -> 0 ou plusieurs args
                                                                                                             # pas avec nargs
    parser.add_argument("--currency", default="eur")            # 2eme arguments -> --currency

    parser.add_argument("--alert",type = float)
    args = parser.parse_args()                                              # Récupère les arguments

    if args.alert:
        try:
            setupPriceAlert(args)
        except ValueError as e:
            print(f"⚠️ Erreur : {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

    try:
        afficherCryptos(args.symbol, args.currency)

    except requests.exceptions.RequestException as e:
        print("❌ Erreur de connexion à l’API CoinGecko :", e)

    except KeyError:
        print(f"⚠️ Crypto '{args.symbol}' ou devise '{args.currency}' non reconnue par l’API.")

    except Exception as e:
        print("❌ Une erreur inattendue est survenue :", e)


if __name__ == "__main__":
    main()
