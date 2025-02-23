import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OMDB_API_KEY")


def get_movie_details(title: str, year: str = "") -> dict:
    url = f"https://www.omdbapi.com/?apikey={api_key}&t={title}&y={year}"
    response = requests.get(url, timeout=10)
    return response.json()


def get_movie_details_by_id(imdb_id: str) -> dict:
    url = f"https://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
    response = requests.get(url, timeout=10)
    return response.json()


def search_movies_by_title(title: str) -> dict:
    url = f"https://www.omdbapi.com/?apikey={api_key}&s={title}"
    response = requests.get(url, timeout=10)
    return response.json()


if __name__ == "__main__":
    movie_details = get_movie_details("DeadStream", "2022")
    print(json.dumps(movie_details, indent=4))

    movie_details_by_id = get_movie_details_by_id("tt1234567")
    print(json.dumps(movie_details_by_id, indent=4))

    search_results = search_movies_by_title("DeadStream")
    print(json.dumps(search_results, indent=4))
