from fastapi import FastAPI, HTTPException
from src.omdb import get_movie_by_title_year, get_movie_details_by_id, search_movies_by_title

app = FastAPI()


@app.get("/movie")
def movie_by_title_year(title: str, year: str = ""):
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    movie_details = get_movie_by_title_year(title, year)
    return movie_details


@app.get("/movie/{imdb_id}")
def movie_by_id(imdb_id: str):
    movie_details = get_movie_details_by_id(imdb_id)
    return movie_details


@app.get("/search")
def search_movies(title: str):
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    search_results = search_movies_by_title(title)
    return search_results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
