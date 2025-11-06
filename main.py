import argparse
from api import get_crypto_price

def main():
    parser = argparse.ArgumentParser(description="Crypto CLI Tracker")
    parser.add_argument("symbol", help="Symbole de la crypto (ex: bitcoin, ethereum, solana)")
    parser.add_argument("--currency", default="usd", help="Devise (usd, eur, etc.)")

    args = parser.parse_args()

    try:
        price = get_crypto_price(args.symbol.lower(), args.currency.lower())
        print(f"💰 {args.symbol.upper()} = {price} {args.currency.upper()}")
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    main()
