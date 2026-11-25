
import os
import requests
from dotenv import load_dotenv

# Load API credentials from the project's .env file
load_dotenv()

API_KEY = os.getenv("DVLA_API_KEY")
API_URL = os.getenv("DVLA_API_URL")

# Check that credentials have been loaded
if not API_KEY or not API_URL:
    raise ValueError("DVLA API credentials are missing. Check your .env file.")

# Enter a vehicle registration number
registration = input("Enter vehicle registration number: ").strip().upper()

# Prepare the API request
headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "registrationNumber": registration
}

try:
    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    print("\nHTTP status:", response.status_code)

    if response.status_code == 200:
        vehicle_data = response.json()

        print("\nVehicle information:")
        for key, value in vehicle_data.items():
            print(f"{key}: {value}")

    else:
        print("\nAPI request unsuccessful.")
        print("Response:", response.text)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)
