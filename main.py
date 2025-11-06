import requests
from rich import print

print("[bold green]Hello from Crypto CLI Tracker APP![/bold green]")

response = requests.get("https://api.coingecko.com/api/v3/ping")
if response.status_code == 200:
    print("[cyan]API OK![/cyan]")
else:
    print("[red]API Error[/red]")
