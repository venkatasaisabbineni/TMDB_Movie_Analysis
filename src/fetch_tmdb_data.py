import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("TMDB_API_KEY")
URL = "https://api.themoviedb.org/3/trending/movie/day"

def fetch_data():
    if not API_KEY:
        raise ValueError("TMDB_API_KEY not found in environment variables.")
    response = requests.get(URL, params={"api_key": API_KEY})
    if response.status_code == 200:
        data = response.json()
        os.makedirs("data", exist_ok=True)
        with open("data/movies.json", "w") as f:
            json.dump(data, f)
        print("Data fetched successfully!")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_data()
