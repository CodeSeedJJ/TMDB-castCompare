import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_movie_cast(movie_id):
    api_key = os.getenv("API_KEY")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        cast_list = [actor["name"] for actor in response.json().get("cast", [])]
        return cast_list
    else:
        print(f"Error fetching cast for movie ID {movie_id}: {response.status_code}")
        return []

def get_tv_series_cast(series_id):
    api_key = os.getenv("API_KEY")
    url = f"https://api.themoviedb.org/3/tv/{series_id}/credits"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        cast_list = [actor["name"] for actor in response.json().get("cast", [])]
        return cast_list
    else:
        print(f"Error fetching cast for series ID {series_id}: {response.status_code}")
        return []

def find_common_actors(movie_id, series_id):
    movie_cast = get_movie_cast(movie_id)
    series_cast = get_tv_series_cast(series_id)
    common_actors = set(movie_cast).intersection(set(series_cast))
    return common_actors

if __name__ == "__main__":
    movie_id = 49521
    series_id = 71912

    common_actors = find_common_actors(movie_id, series_id)
    print("Common actors between the movie and the TV series:")
    print(common_actors)
