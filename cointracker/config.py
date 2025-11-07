# cointracker/config.py
import json
import os

CONFIG_PATH = "config.json"

default_config = {
    "currency": "EUR",
    "favorites": ["bitcoin", "ethereum"],
    "api_source": "coingecko"
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        save_config(default_config)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
