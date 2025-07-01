# 📍 Nominatim API Tutorial

This project demonstrates how to convert client addresses into geographic coordinates (latitude/longitude) using the Deploily Nominatim API, store them in a SQLite database, and visualize clients on a map using Leaflet.js and Flask.

---

## 📦 Introduction

The Nominatim API is a geolocation service based on OpenStreetMap that allows you to:

    🔁 Convert addresses to coordinates (forward geocoding)

    📌 Visualize addresses on maps

    🧭 Calculate nearby delivery points (future enhancement)

This project shows how to integrate this API in a Python environment for logistics, mapping, delivery, and geo-analytics.

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
```bash
export API_KEY=your_api_key_here
```

##  🚀 How It Works
### 1️⃣ Geocode Client Addresses

Run the geocoding script:
```bash
python3 nominatim.py
```

This will:

 Query the Deploily API

 Fetch GPS coordinates for each address

 Store them in the clients.db SQLite database

 python3 app.py

### 2️⃣ Launch the Flask App
Run the geocoding script:
```bash
python3 app.py
```

Then open your browser at:

http://localhost:5000



You will see all your clients placed on a map with markers, each showing:

Client name

Geocoded address

 ## 🧾 requirements.txt