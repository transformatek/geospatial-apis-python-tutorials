# 🧭 Nominatim API Tutorial

Ce projet démontre comment utiliser l'API Nominatim de Deploily pour convertir des adresses en coordonnées GPS (géocodage) et vice versa (reverse géocoding), puis stocker et visualiser les données dans une base locale SQLite.
---

## 📦 Introduction

The Nominatim API helps you convert addresses into GPS coordinates and GPS coordinates back into readable addresses.

Use it when you want to:

🗺️ Plot clients or delivery addresses on a map

📍 Auto-detect locations in your apps

🚚 Optimize delivery or logistics routes

📊 Power geospatial analysis with structured data


---

##  🗂️ Project Structure

```bash
nominatim-flask-map/
│
├── nominatim.py        
├── app.py               
├── templates/
│   └── map.html         
├── clients.db          
├── requirements.txt    
└── README.md       
```

## 🔁 Clone the repository
```bash
git clone https://github.com/transformatek/geospatial-apis-python-tutorials.git
cd geospatial-apis-python-tutorials
```
## ⚙️ Environment Setup

🔧 Install required Python packages

```bash
pip install -r requirements.txt
```
🔐 Set your Deploily API key

Before running the script, export your Deploily API key:
```bash
export API_KEY=your_api_key_here
```
##  🚀 How It Works
### ✅ 1. Load the API Key
```bash
API_KEY = os.getenv("API_KEY")
```
### 🌐 2. Make API Call to Geocode Address
```bash
params = {"q": "El Mouradia, Alger", "format": "json"}
response = requests.get("https://api.deploily.cloud/nominatim/search", params=params, headers=HEADERS_JSON)
```
### 🗃️ 3. Create SQLite Database
The script creates a clients.db file with a clients table

### 🧭 4. Add Clients and Geocode
The script loops through a list of client addresses, retrieves coordinates via the API, and inserts the data into the database.

```bash
📦 Initialising DB...
📍 Adding clients from addresses...
✅ Client A → (35.3032, -1.1418)
```
### 📤 Example Output
```bash
Status: 200
[
  {
    "place_id": 499352,
    "lat": "36.7473392",
    "lon": "3.0506705",
    "name": "El Mouradia",
    "display_name": "El Mouradia, Daïra Sidi M'Hamed, Alger, Algérie"
  }
]
```
| Field           | Description                                                                |
|-----------------|----------------------------------------------------------------------------|
| `status`        | Indicates the result of the API call. `"Success"` means the call succeeded.|
| `place_id `     | Unique ID for the location                                                 |
| `lat / lon`     |Geographic coordinates (latitude/longitude)                                 |
| `name `         | Short name of the location                                                 |
| `display_name ` | Full address (ideal for UI or maps)                                        |

### Run the geocoding script

```bash
python3 nominatim.py
```

### Launch the Flask App

Run the geocoding script:
```bash
python3 app.py
```

### open your browser at:
```bash
http://localhost:5000
```
You will see all your clients placed on a map with markers

## 📁 Script Location

[➡️ nominatim.py](./nominatim.py)

## Useful links 
- [https://docs.deploily.cloud/docs/nominatim](https://docs.deploily.cloud/docs/nominatim)

- [https://docs.deploily.cloud/nominatim-api/#/](https://docs.deploily.cloud/nominatim-api/#/)

- [https://deploily.cloud/](https://deploily.cloud/)