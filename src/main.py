import requests

# URL for testing: https://musicbrainz.org/ws/2/release?'limit=1&query=Chasing-Cars-Part&fmt=json
song = "Chasing-Cars-Part"  # replace with your song title
response = requests.get(
    f"https://musicbrainz.org/ws/2/release?'limit=1&query={song}&fmt=json"
)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Check if there are any recordings in the response
    if data["releases"]:
        first_recording = data["releases"][0]
        print("Title:", first_recording["title"])

        # Check if there are any artist credits in the first recording
        if first_recording["artist-credit"]:
            print("Artist:", first_recording["artist-credit"][0]["name"])
        else:
            print("No artist credit found.")
    else:
        print("No recordings found.")
else:
    print("Error:", response.status_code)
