import requests
import time
import pandas as pd

def fetch_data(max_pages=20, vs_currency="usd"):
    url = "https://api.coingecko.com/api/v3/coins/markets"

    data_all = []
    page = 1

    max_retries = 5
    retries = 0

    while page <= max_pages:
        params = {
            "vs_currency": vs_currency,
            "order": "market_cap_desc",
            "per_page": 250,
            "page": page,
            "sparkline": "false"
        }

        response = requests.get(url, params=params)

        # Gestion des limites API
        if response.status_code == 429:
            retries += 1
            print(f"limit ({retries}/{max_retries})")

            if retries >= max_retries:
                print("Trop de rate limit → arrêt du script")
                break

            time.sleep(15)
            continue

        # Autres erreurs API
        if response.status_code != 200:
            print("Erreur :", response.text)
            break

        retries = 0  # reset si succès

        data = response.json()

        # Fin des données
        if not data:
            print("Fin des données")
            break

        data_all.extend(data)
        print(f"Page {page} récupérée, total : {len(data_all)}")

        page += 1
        time.sleep(3)

    # DataFrame
    df = pd.DataFrame(data_all)

    if not df.empty:
        cols = ["id", "symbol", "name", "current_price", "market_cap", "total_volume"]
        df = df[cols]
        print(df.head())
    else:
        print("Aucune donnée récupérée")

    return df