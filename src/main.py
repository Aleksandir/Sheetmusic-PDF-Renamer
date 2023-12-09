import os

import requests

# URL for testing: https://musicbrainz.org/ws/2/release?limit=1&query=Chasing-Cars-Part&fmt=json


testFiles_dir = "testFiles"  # replace with your directory


def main():
    for filename in os.listdir(testFiles_dir):
        base_name, ext = os.path.splitext(filename)
        title, artist = get_title_and_artist(base_name)
        print(f"Base name: {base_name}\n{title} - {artist}\n")


def get_title_and_artist(song):
    response = requests.get(
        f"https://musicbrainz.org/ws/2/release?limit=1&query={song}&fmt=json"
    )

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if there are any recordings in the response
        if data["releases"]:
            first_recording = data["releases"][0]
            title = first_recording["title"]

            # Check if there are any artist credits in the first recording
            if first_recording["artist-credit"]:
                artist = first_recording["artist-credit"][0]["name"]
            else:
                artist = "No artist credit found."
        else:
            title = "No recordings found."
            artist = "No recordings found."
    else:
        title = "Error"
        artist = "Error"

    return title, artist


main()
