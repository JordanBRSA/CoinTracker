import sys
import argparse
from cointracker.api import get_crypto_price
from cointracker.config import load_config, save_config

def main():
    # Cas spécial : changer la devise
    if len(sys.argv) > 2 and sys.argv[1] == "set-currency":
        new_currency = sys.argv[2].upper()
        config = load_config()
        config["currency"] = new_currency
        save_config(config)
        print(f"✅ Devise changée en {new_currency}")
        return

    # Charger la configuration
    config = load_config()

    # Parser les arguments pour une requête normale
    parser = argparse.ArgumentParser(description="Crypto CLI Tracker")
    parser.add_argument("symbol", nargs="?", help="Symbole de la crypto (ex: bitcoin, ethereum, solana)")
    parser.add_argument("--currency", help=f"Devise (par défaut : {config['currency']})")

    args = parser.parse_args()

    # Si aucun symbole → afficher la config
    if not args.symbol:
        print(f"💾 Configuration actuelle :")
        print(f"  Devise par défaut : {config['currency']}")
        print(f"  Cryptos favorites : {', '.join(config['favorites'])}")
        return

    # Utiliser la devise passée ou celle du fichier config
    currency = args.currency.lower() if args.currency else config["currency"].lower()

    # Appel API
    try:
        price = get_crypto_price(args.symbol.lower(), currency)
        print(f"💰 {args.symbol.upper()} = {price} {currency.upper()}")
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    main()
