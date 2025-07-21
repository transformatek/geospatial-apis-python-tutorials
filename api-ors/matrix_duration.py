import os
import json
import requests

# export API_KEY=......
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise SystemExit("API_KEY environment variable not set!")

HEADERS_JSON = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "apikey": API_KEY,
}


def print_result(response):
    """Afficher proprement la réponse"""
    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False)[:800] + "…")
    except ValueError:
        print("Response is not JSON.")
        print(response.text[:800] + "…")
    print("-" * 60)


def test_matrix_duration():
    print("Test Matrix Duration")
    url = "https://api.deploily.cloud/ors/v2/matrix/driving-car"

    payload = {
        "locations": [
            [3.0588, 36.7538],
            [1.8992, 35.6971],
            [5.3698, 36.7081],
            [0.1402, 35.3733],
        ],
        "id": "my_request",
        "sources": ["all"],
        "destinations": ["all"],
        "metrics": ["duration"],
        "resolve_locations": False,
        "units": "m",
    }

    response = requests.post(url, headers=HEADERS_JSON, json=payload)
    print_result(response)


if __name__ == "__main__":
    test_matrix_duration()
