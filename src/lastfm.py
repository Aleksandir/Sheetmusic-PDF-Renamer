import os
import pprint

import requests
from dotenv import load_dotenv


def get_title_and_artist(song):
    load_dotenv()

    APIKEY = os.getenv("LASTFM_API_KEY")

    response = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=track.search&track={song}&api_key={APIKEY}&format=json"
    )

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if there are any recordings in the response
        if data["results"]["trackmatches"]["track"]:
            title = data["results"]["trackmatches"]["track"][0]["name"]
            artist = data["results"]["trackmatches"]["track"][0]["artist"]
        else:
            title = "Error"
            artist = "Error"

    return title, artist


if __name__ == "__main__":
    title, artist = get_title_and_artist("Kickstart My Heart Mötley Crüe")
    print(title)
    print(artist)
