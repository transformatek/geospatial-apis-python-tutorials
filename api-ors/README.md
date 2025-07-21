# 📍 ORS Matrix API Tutorial

This project demonstrates how to calculate travel durations and distances between multiple geographic points using the ORS Matrix API with the [Deploily API](https://api.deploily.cloud/).

---

## 📦 Introduction

The ORS Matrix API allows you to compute distance and duration matrices for a list of locations. It supports various travel modes like driving, walking, and cycling. This is particularly useful for logistics, route optimization, and location analysis. The API requires secure access via API keys.

---
## 🔁 Clone the repository

```bash
git clone https://github.com/transformatek/geospatial-apis-python-tutorials.git
cd geospatial-apis-python-tutorials
```

## ⚙️ Environment Setup
```bash
export API_KEY= your_api_key
```
## 🚀 How the script works

✅ 1. Export API key
```bash
API_KEY = os.getenv("API_KEY")
```
🌐 2. Call the API
```bash
url = "https://api.deploily.cloud/ors/v2/matrix/driving-car"
headers = {
    "Accept": "application/json;charset=UTF-8, */*",
    "Content-Type": "application/json",
    "apikey": API_KEY
}
payload = {
  "locations": [[8.681495, 49.41461], [8.687872, 49.420318]],
  "metrics": ["duration", "distance"],
  "units": "km"
}

```
📤 3. Output example

```bash
Status: 200
{
  "distances": [[0.0, 1.1], [1.1, 0.0]],
  "durations": [[0.0, 60.2], [60.3, 0.0]]
}
```
| Field       | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| `distances` | A matrix showing the distances (in kilometers) between points.     |
| `durations` | A matrix showing the travel durations (in seconds) between points. |

📁 Script Location

[➡️ matrix_duration.py](./matrix_duration.py)

## Useful links 
- [https://docs.deploily.cloud/docs/ors](https://docs.deploily.cloud/docs/ors)
- [https://deploily.cloud/](https://deploily.cloud/)
- [https://docs.deploily.cloud/docs/ors](https://docs.deploily.cloud/docs/ors)