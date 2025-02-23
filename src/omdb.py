import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OMDB_API_KEY")


def get_movie_by_title_year(title: str, year: str = "") -> dict:
    """
    Fetches movie details by title and optional year.

    Args:
        title (str): The title of the movie.
        year (str, optional): The year of the movie. Defaults to "".

    Returns:
        dict: The movie details.
    """
    url = f"https://www.omdbapi.com/?apikey={api_key}&t={title}&y={year}"
    response = requests.get(url, timeout=10)
    return response.json()


def get_movie_details_by_id(imdb_id: str) -> dict:
    """
    Fetches movie details by IMDb ID.

    Args:
        imdb_id (str): The IMDb ID of the movie.

    Returns:
        dict: The movie details.
    """
    url = f"https://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
    response = requests.get(url, timeout=10)
    return response.json()


def search_movies_by_title(title: str) -> dict:
    """
    Searches for movies by title.

    Args:
        title (str): The title of the movie to search for.

    Returns:
        dict: The search results.
    """
    url = f"https://www.omdbapi.com/?apikey={api_key}&s={title}"
    response = requests.get(url, timeout=10)
    return response.json()
