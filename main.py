from cointracker.api import get_crypto_price
from plyer import notification
import argparse
import requests
import sys


def main():

    parser = argparse.ArgumentParser()                                      # Permet de pouvoir saisir des arguments dans le terminal
    parser.add_argument("symbol",nargs="*",default="bitcoin")  # 1er arguments -> symbol        # nargs = * -> 0 ou plusieurs args
                                                                                                             # pas avec nargs
    parser.add_argument("--currency", default="eur")            # 2eme arguments -> --currency

    parser.add_argument("--alert",type = float)
    args = parser.parse_args()                                              # Récupère les arguments

    try:
        if args.alert and len(args.symbol) > 1:
            print("Veuillez saisir une seule crypto pour mettre une alerte.")
            sys.exit()

        elif args.alert:
            print(f"⚠️ Alerte mise en place pour {args.symbol[0]}  à {args.alert} {args.currency}")

            price = get_crypto_price(args.symbol[0], args.currency)

            if price == args.alert:
                notification.notify(
                    title=f"Alerte {args.symbol[0]}",
                    message=f"{args.symbol[0]} a atteint {price} {args.currency} !",
                    timeout=5
                )
    except Exception as e:
        print(f"Erreur lors de la mise en place de l'alerte : {e}")



    try:
        print("__________CoinTrakcer__________\n")
        for coin in args.symbol :
            price = get_crypto_price(coin, args.currency)            # Appel de la fonction avec les paramètres du terminal
            print(f"Valeur de {coin} : {price} {args.currency}")
            print("____________________\n")

    except requests.exceptions.RequestException as e:
        print("❌ Erreur de connexion à l’API CoinGecko :", e)

    except KeyError:
        print(f"⚠️ Crypto '{args.symbol}' ou devise '{args.currency}' non reconnue par l’API.")

    except Exception as e:
        print("❌ Une erreur inattendue est survenue :", e)

if __name__ == "__main__":
    main()
