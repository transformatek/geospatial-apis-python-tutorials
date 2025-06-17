import os
import json
import requests

# export API_KEY=......
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise SystemExit("❌  API_KEY environment variable not set!")

HEADERS_JSON = {
    "Accept": "application/json",
    "apikey": API_KEY,
}


def print_result(response):
    """Pretty‑print the outcome of a call."""
    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False)[:800] + "…")
    except ValueError:
        print("❌  Response is not JSON.")
        print(response.text[:800] + "…")
    print("-" * 60)


# 1️⃣  GET wilaya
def test_get_wilaya():
    print("🔍 getWilaya")
    url = "https://api.deploily.cloud/wilaya/api/v1/getWilaya"
    params = {"lat": 35, "long": -1.1}
    r = requests.get(url, params=params, headers=HEADERS_JSON)
    print_result(r)


if __name__ == "__main__":
    test_get_wilaya()
