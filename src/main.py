import os
import string

import requests

# URL for testing: https://musicbrainz.org/ws/2/release?limit=1&query=Chasing-Cars-Part&fmt=json


def main():
    print("Scanning directory...")
    names, differences = scan_dir("testFiles/")

    # print the differences
    for i in range(len(differences)):
        print(differences[i])

    print("\n\n\n")
    for i in range(len(names)):
        print(f"testFiles/{names[i]}")

    while True:
        print("\n\n\n")
        print("1. Rename files")
        print("2. ignore file")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Renaming files...")
            # rename_files(names)
        elif choice == "2":
            index = -1
            while True:
                index = int(input(f"Enter index of file between 0 and {len(names)}: "))
                if index < 0 or index >= len(names):
                    print("Invalid index.")
                else:
                    break
            print(f"Ignoring file - {names[index]}")
            # ignore_file(index)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def scan_dir(dir):
    new_names = []
    differences = []
    index = 0
    for filename in os.listdir(dir):
        base_name, ext = os.path.splitext(filename)
        title, artist = get_title_and_artist(base_name)

        newName = f"{title} - {artist}{ext}"
        # Remove punctuation from the new name except for "-" and "."
        for char in newName:
            if char in string.punctuation and not char == "-" and not char == ".":
                newName = newName.replace(char, "")

        base_name = str(index) + ". " + base_name
        index += 1
        if len(base_name) > 50:
            base_name = base_name[:47] + "..."

        new_names.append(newName)
        differences.append(f"{base_name.ljust(50)} =>          {newName}")
    return new_names, differences


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
