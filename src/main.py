import os
import string

from lastfm import get_title_and_artist
from tqdm import tqdm

directory = input("Enter directory: ")


def main():
    print("Scanning directory...")

    names, differences = scan_dir(directory)

    # print the differences
    display_differences(differences, names)

    while True:
        print("\n")
        print("1. Rename files")
        print("2. Ignore files")
        print("3. Undo ignore file")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Renaming files...")
            rename_files(names, differences)
            print("Done.")
            break
        elif choice == "2":
            index = -1
            while True:
                # validate input
                indices = input(
                    f"Enter indices of files between 0 and {len(names)-1}, separated by spaces: "
                )
                indices = [int(index) for index in indices.split()]

                if any(index < 0 or index >= len(names) for index in indices):
                    print("Invalid index.")
                else:
                    break

            names = ignore_file(indices, names, differences)
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
    # add a line break
    print()
    for key, value in differences.items():
        if len(differences[key][0]) > 50:
            short_name = differences[key][0][: 47 - len(str(key))] + "..."
            print(
                f"{key}. {short_name} => {names[key][:70]}{'...' if len(names[key]) > 70 else ''}"
            )
        else:
            print(
                f"{key}. {differences[key][0].ljust(50-len(str(key)))} => {names[key][:70]}{'...' if len(names[key]) > 70 else ''}"
            )


def rename_files(names, differences):
    for index, new_name in enumerate(names):
        if new_name == "ignored":
            continue

        original_filename = differences[index][0]
        new_path = f"{directory}/{new_name}.pdf"

        # Check if a file with the new name already exists
        counter = 1
        while os.path.exists(new_path):
            new_path = f"{directory}/{new_name}({counter}).pdf"
            counter += 1

        os.rename(f"{directory}/{original_filename}", new_path)


def ignore_file(list_of_index, new_names, differences):
    """
    Ignores files based on the given list of indices.

    Args:
        list_of_index (list): List of indices of files to be ignored.
        new_names (list): List of new names for the files.
        differences (list): List of file differences.

    Returns:
        list: Updated list of new names.
    """
    # to separate the new names from the old names
    print()
    for index in list_of_index:
        print(f"Ignoring file - {differences[index][1]}")
        new_names[index] = "ignored"

    display_differences(differences, new_names)

    return new_names


def scan_dir(dir):
    """
    Scans the specified directory and renames the files based on their title and artist.

    Args:
        dir (str): The directory path to scan.

    Returns:
        tuple: A tuple containing a list of new file names and a dictionary of differences between the old and new names.
    """
    new_names = []
    errors = []
    differences = {}
    index = 0
    for filename in tqdm(os.listdir(dir)):
        base_name, ext = os.path.splitext(filename)

        # Only consider .pdf files
        if ext.lower() != ".pdf":
            continue

        title, artist = get_title_and_artist(base_name)

        if title == "Error" or artist == "Error":
            errors.append(filename)
            continue

        new_name = f"{title} - {artist}"
        # Remove punctuation from the new name except for "-" and "."
        for char in new_name:
            if char in string.punctuation and not char == "-" and not char == ".":
                new_name = new_name.replace(char, "")

        differences[index] = [filename, new_name]  # Use the index as the key
        new_names.append(new_name)
        index += 1
    for i in errors:
        print(f"No result found for: {i}")
    return new_names, differences


if __name__ == "__main__":
    main()
