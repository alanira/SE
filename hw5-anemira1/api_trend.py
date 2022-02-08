import requests
import json
import os
from dotenv import find_dotenv, load_dotenv
# take API key - keep API safe
# take base URL HTTPS request
# API request https://api.themoviedb.org/3/trending/all/day?api_key=2043941d3481edb6a955d390b150517f 20k

# get trending GET/trending/{media_type}/{time_window}
# https://developers.themoviedb.org/3/trending/get-trending



 # API key from TMDB
BASE_URL="https://api.themoviedb.org/3/trending/movie/week" # search trending movies of the day/week also possible

load_dotenv(find_dotenv())

API_KEY = os.getenv("NYT_KEY")
query_param = {
    "api_key": API_KEY,
}

response = requests.get( # response from NYT API
    BASE_URL,
    params=query_param,
)


movies = response.json()["results"] # take info that you need from json file
#print(movies)
for movie in movies[0:10]:
    print(movie["title"])

# code .env file
# in same folder
# code .gitignore <- .env file