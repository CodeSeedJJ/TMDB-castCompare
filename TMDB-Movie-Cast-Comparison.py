# This script is old and messy on purpose.
# Please enjoy my humble beginnings. -JayJay


import dotenv
from dotenv import load_dotenv
import os
import requests

def get_series_cast(series_id, api_key):
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
    cast1 = get_series_cast(series1_id, api_key)
    cast2 = get_series_cast(series2_id, api_key)
    common_actors = set(cast1).intersection(set(cast2))
    return common_actors

if __name__ == "__main__":
    API_KEY = "******"
    series1_id = 71712
    series2_id = 118

    common_actors = find_common_actors(API_KEY, series1_id, series2_id)
    print("Common actors between the two movies:")
    print(common_actors)
