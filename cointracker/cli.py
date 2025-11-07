# cointracker/cli.py
from cointracker.config import load_config, save_config

def set_currency(new_currency: str):
    config = load_config()
    config["currency"] = new_currency.upper()
    save_config(config)
    print(f"✅ Devise changée en {config['currency']}")

def show_config():
    config = load_config()
    print("Configuration actuelle :")
    for k, v in config.items():
        print(f"  {k}: {v}")
