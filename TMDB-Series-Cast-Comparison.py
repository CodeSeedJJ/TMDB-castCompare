import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def get_tv_series_cast(series_id, api_key):
    url = f"https://api.themoviedb.org/3/tv/{series_id}/credits"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        cast_list = [actor["name"] for actor in response.json().get("cast", [])]
        return cast_list
    else:
        print(f"Error fetching cast for series ID {series_id}: {response.status_code}")
        return []

def find_common_actors(api_key, series1_id, series2_id):
    cast1 = get_tv_series_cast(series1_id, api_key)
    cast2 = get_tv_series_cast(series2_id, api_key)
    common_actors = set(cast1).intersection(set(cast2))
    return common_actors

if __name__ == "__main__":
    # Fetch the API key from the .env file
    API_KEY = os.getenv("API_KEY")
    
    series1_id = 71712
    series2_id = 118

    common_actors = find_common_actors(API_KEY, series1_id, series2_id)
    print("Common actors between the two TV series:")
    print(common_actors)
