
import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

# Locate and load the project's .env file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Load DVSA credentials
CLIENT_ID = os.getenv("DVSA_CLIENT_ID")
CLIENT_SECRET = os.getenv("DVSA_CLIENT_SECRET")
API_KEY = os.getenv("DVSA_API_KEY")
SCOPE = os.getenv("DVSA_SCOPE")
TOKEN_URL = os.getenv("DVSA_TOKEN_URL")

# Check credentials
if not all([CLIENT_ID, CLIENT_SECRET, API_KEY, SCOPE, TOKEN_URL]):
    raise ValueError("One or more DVSA credentials are missing.")

def get_access_token():
    """Request an OAuth access token from DVSA's identity provider."""

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": SCOPE
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(
        TOKEN_URL,
        data=payload,
        headers=headers,
        timeout=30
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Token request failed: HTTP {response.status_code}"
        )

    token_data = response.json()

    access_token = token_data.get("access_token")

    if not access_token:
        raise RuntimeError("No access token returned.")

    return access_token



from urllib.parse import quote

def get_mot_history(registration, access_token):
    """Retrieve MOT history for a vehicle registration."""

    endpoint = (
        "https://history.mot.api.gov.uk/"
        f"v1/trade/vehicles/registration/{quote(registration, safe='')}"
    )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-API-Key": API_KEY,
        "Accept": "application/json"
    }

    response = requests.get(
        endpoint,
        headers=headers,
        timeout=30
    )

    print("MOT API HTTP status:", response.status_code)

    if response.status_code == 200:
        return response.json()

    print("API error:", response.text)
    return None


if __name__ == "__main__":
    try:
        registration = input(
            "Enter vehicle registration number: "
        ).strip().upper()

        print("\nRequesting DVSA access token...")
        token = get_access_token()
        print("Authentication successful.")

        print("\nRequesting MOT history...")
        mot_data = get_mot_history(registration, token)

        if mot_data is not None:
            print("\nMOT history retrieved successfully!")
            print(json.dumps(mot_data, indent=4))

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)

    except RuntimeError as error:
        print("Authentication error:", error)
