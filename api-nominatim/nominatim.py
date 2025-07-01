# nominatim.py
import os
import requests
import sqlite3
# export API_KEY=""

# Lire la clé API depuis la variable d’environnement
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise SystemExit("❌ API_KEY environment variable not set!")

# URL pour l'opération adresse → coordonnées
API_URL = "https://api.deploily.cloud/nominatim/search"


#  Fonction pour récupérer les coordonnées à partir d'une adresse
def get_coordinates(address):
    params = {"q": address, "format": "json", "accept-language": "fr"}
    headers = {"Accept": "application/json", "apikey": API_KEY}

    response = requests.get(API_URL, params=params, headers=headers)
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


#  Création de la base de données
def create_db():
    conn = sqlite3.connect("clients.db")
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            latitude REAL,
            longitude REAL,
            address TEXT
        )
    """
    )
    conn.commit()
    conn.close()


#  Ajout de clients à partir d'adresses (géocodage direct)
def add_clients_from_address():
    clients = [
        {"name": "Client A", "address": "Rue Guettaï Kacem, Ain Temouchent"},
        {"name": "Client B", "address": "El Mouradia, Alger"},
        {"name": "Client C", "address": "Chehaima, Tiaret"},
    ]

    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()

    for client in clients:
        lat, lon = get_coordinates(client["address"])
        if lat is not None and lon is not None:
            print(f"{client['name']} → ({lat}, {lon})")
            cursor.execute(
                """
                INSERT INTO clients (name, latitude, longitude, address)
                VALUES (?, ?, ?, ?)
            """,
                (client["name"], lat, lon, client["address"]),
            )
        else:
            print(f"⚠️ Client {client['name']} non inséré (adresse invalide).")

    conn.commit()
    conn.close()


#  Point d'entrée principal
if __name__ == "__main__":
    create_db()
    add_clients_from_address()
