import requests

# current bugs
# 1 sometimes returns artist as song title (Iris-The-Goo-Goo-Dolls-Peter-John-Arrangeme... => Goo Goo Dolls - Goo Goo Dolls) & (Poison - Alice-Cooper => Alice Cooper - Alice Cooper)
# 2 sometimes gets the artist wrong and instead has another artist or uses a cover artist (creep chords => Creep - VELIAL SQUAD, Stairway to heven => Heven - O Saala Sakraal)


def get_title_and_artist(song):
    """
    Retrieves the title and artist of a song from the MusicBrainz API.

    Args:
        song (str): The name of the song.

    Returns:
        tuple: A tuple containing the title and artist of the song.
    """
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
