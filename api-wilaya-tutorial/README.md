# 📍 Wilaya API Tutorial

This project demonstrates how to retrieve wilaya (province) information in Algeria using geographic coordinates with the [Deploily API](https://api.deploily.cloud/).

---

## 📦 Introduction

The Wilaya/Commune API helps you find commune and wilaya details using geographic coordinates. Simply provide latitude and longitude to get accurate location data. It’s useful for mapping, address lookup, and location-based services. Secure access is ensured with API keys .

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
url = "https://api.deploily.cloud/wilaya/api/v1/getWilaya"
params = {"lat": 35, "long": -1.1}
```
📤 3. Output example

```bash
Status: 200
{
  "status": "Success",
  "data": {
    "wilaya": {
      "id": 13,
      "code": 13,
      "nom": "Tlemcen",
      "nom_maj": "TLEMCEN",
      "nom_ar": "تلمسان"
    }
  }
}
```

| Field           | Description                                                                |
|-----------------|----------------------------------------------------------------------------|
| `status`        | Indicates the result of the API call. `"Success"` means the call succeeded. |
| `data`          | Contains the actual result of the query.                                   |
| `wilaya.id`     | Internal numeric ID of the wilaya in the database.                         |
| `wilaya.code`   | Official administrative code for the wilaya.                               |
| `wilaya.nom`    | Name of the wilaya in French (normal case).                                |
| `wilaya.nom_maj`| Name of the wilaya in UPPERCASE letters.                                   |
| `wilaya.nom_ar` | Name of the wilaya in Arabic script.                                       |



📁 Script Location


[➡️ wilaya.py](./wilaya.py)

## Useful links 

- [https://docs.deploily.cloud/docs/wilaya-commune](https://docs.deploily.cloud/docs/wilaya-commune)
- [https://github.com/deploily/api-wilaya-commune](https://github.com/deploily/api-wilaya-commune)
- [https://docs.deploily.cloud/wilaya-commune-api/#/](https://docs.deploily.cloud/wilaya-commune-api/#/)
- [https://deploily.cloud/](https://deploily.cloud/)
- [https://hub.deploily.cloud/blog/deploily-apis-3/accurate-wilaya-lookup-in-algeria-using-latitude-longitude-11](https://hub.deploily.cloud/blog/deploily-apis-3/accurate-wilaya-lookup-in-algeria-using-latitude-longitude-11)

