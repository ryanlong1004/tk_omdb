# OMDB API Wrapper

This project provides a simple Python wrapper for the OMDB API.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your OMDB API key:
   ```dotenv
   OMDB_API_KEY=your_api_key_here
   ```

## Usage

The `omdb.py` script provides the following functions:

### `get_movie_details(title: str, year: str = "") -> dict`

Fetches movie details by title and optional year.

### `get_movie_details_by_id(imdb_id: str) -> dict`

Fetches movie details by IMDb ID.

### `search_movies_by_title(title: str) -> dict`

Searches for movies by title.

### Example

```python
import json
from omdb import get_movie_details, get_movie_details_by_id, search_movies_by_title

movie_details = get_movie_details("DeadStream", "2022")
print(json.dumps(movie_details, indent=4))

movie_details_by_id = get_movie_details_by_id("tt1234567")
print(json.dumps(movie_details_by_id, indent=4))

search_results = search_movies_by_title("DeadStream")
print(json.dumps(search_results, indent=4))
```
