import os
import string

import requests

# URL for testing: https://musicbrainz.org/ws/2/release?limit=1&query=Chasing-Cars-Part&fmt=json


def main():
    print("Scanning directory...")
    names, differences = scan_dir("testFiles/")

    # print the differences
    display_differences(differences, names)

    while True:
        print("\n")
        print("1. Rename files")
        print("2. ignore file")
        print("3. undo ignore file")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Renaming files...")
            rename_files(names)
        elif choice == "2":
            index = -1
            while True:
                # validate input
                index = int(input(f"Enter index of file between 0 and {len(names)}: "))
                if index < 0 or index >= len(names):
                    print("Invalid index.")
                else:
                    break

            print(f"Ignoring file - {names[index]}")
            names = ignore_file(index, names, differences)
        elif choice == "3":
            index = -1
            while True:
                # validate input
                index = int(
                    input(f"Enter index of file between 0 and {len(names)-1}: ")
                )
                if index < 0 or index >= len(names):
                    print("Invalid index.")
                else:
                    break

            undo_ignored_file(index, names, differences)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def undo_ignored_file(index, names, differences):
    print(f"Undoing ignore file - {differences[index][1]}")
    if differences.get(index):  # Check if index exists in differences
        names[index] = differences[index][1]
        print(f"New name - {names[index]}")
    else:
        print(f"No proposed new name for - {differences[index][0]}")

    display_differences(differences, names)


def display_differences(differences, names):
    for key, value in differences.items():
        print(f"{differences[key][0].ljust(50)} => {names[key]}")


def rename_files(names):
    index = 0
    for filename in os.listdir("testFiles/"):
        base_name, ext = os.path.splitext(filename)
        if names[index] == "ignored":
            index += 1
            continue

        os.rename(f"testFiles/{filename}", f"testFiles/{names[index]}{ext}")
        index += 1


def ignore_file(index, new_names, differences):
    # to separate the new names from the old names
    print()
    new_names[index] = "ignored"

    display_differences(differences, new_names)

    return new_names


def scan_dir(dir):
    new_names = []
    differences = {}
    index = 0
    for filename in os.listdir(dir):
        base_name, ext = os.path.splitext(filename)
        title, artist = get_title_and_artist(base_name)

        new_name = f"{title} - {artist}"
        # Remove punctuation from the new name except for "-" and "."
        for char in new_name:
            if char in string.punctuation and not char == "-" and not char == ".":
                new_name = new_name.replace(char, "")

        base_name = str(index) + ". " + base_name
        if len(base_name) > 50:
            base_name = base_name[:47] + "..."

        differences[index] = [base_name, new_name]  # Use the index as the key
        new_names.append(new_name)
        index += 1

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
