# nominatim.py

import os
import json
import requests
import sqlite3

# 🔐 Exporter d'abord ta clé : export API_KEY="your_api_key"
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise SystemExit("❌ API_KEY environment variable not set!")

HEADERS_JSON = {
    "Accept": "application/json",
    "apikey": API_KEY,
}

API_URL = "https://api.deploily.cloud/nominatim/search"

# 🧾 Pretty-print des réponses API
def print_result(response):
    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False)[:800] + "…")
    except ValueError:
        print("❌  Response is not JSON.")
        print(response.text[:800] + "…")
    print("-" * 60)


# 📍 Fonction de géocodage
def get_coordinates(address):
    params = {"q": address, "format": "json", "accept-language": "fr"}
    response = requests.get(API_URL, params=params, headers=HEADERS_JSON)
    print_result(response)

    if response.status_code == 200:
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
        else:
            print(f"⚠️ Adresse non trouvée : {address}")
            return None, None
    else:
        print(f"❌ Erreur API pour {address} : {response.status_code}")
        return None, None


# 🗃️ Création DB SQLite
def create_db():
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            latitude REAL,
            longitude REAL,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()


# ➕ Ajout clients à partir d'adresses
def add_clients():
    clients = [
        {"name": "Client A", "address": "Rue Guettaï Kacem, Ain Temouchent"},
        {"name": "Client B", "address": "El Mouradia, Alger"},
        {"name": "Client C", "address": "Chehaima, Tiaret"},
    ]

    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()

    for client in clients:
        lat, lon = get_coordinates(client["address"])
        if lat and lon:
            print(f"✅ {client['name']} → ({lat}, {lon})")
            cursor.execute("""
                INSERT INTO clients (name, latitude, longitude, address)
                VALUES (?, ?, ?, ?)
            """, (client["name"], lat, lon, client["address"]))
        else:
            print(f"❌ Client {client['name']} non inséré (adresse invalide).")

    conn.commit()
    conn.close()


# 🚀 Main
if __name__ == "__main__":
    print("📦 Initialisation DB...")
    create_db()
    print("📍 Ajout des clients depuis les adresses...")
    add_clients()
