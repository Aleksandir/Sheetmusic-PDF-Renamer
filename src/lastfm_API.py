import os

import requests
from dotenv import load_dotenv


def get_title_and_artist(song: str) -> tuple[str, str]:
    load_dotenv()

    APIKEY = os.getenv("LASTFM_API_KEY")

    response = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=track.search&limit=1&track={song}&api_key={APIKEY}&format=json"
    )

    title = "Error"
    artist = "Error"

    if response.status_code == 200:
        data = response.json()

        # Check if there are any recordings in the response
        if data["results"]["trackmatches"]["track"]:
            title = data["results"]["trackmatches"]["track"][0]["name"]
            artist = data["results"]["trackmatches"]["track"][0]["artist"]

    return title, artist
