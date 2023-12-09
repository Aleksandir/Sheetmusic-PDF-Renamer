# MusicBrainz PDF Renamer 🎵

This project is a Python program that renames sheet music PDF files in a directory using the MusicBrainz API. The program takes the existing file names, which are assumed to be song names, and queries the MusicBrainz API to get the correct song name and artist name. The PDF files are then renamed to the format "Song name - Artist name" 🎶🎨

## Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋

- Python 3.7 or later 🐍
- A MusicBrainz account to get API credentials 🔑

### Installing 💻

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Install the necessary dependencies by running `pip install -r requirements.txt` 📦

### Usage 🎯

1. Run the program with `python main.py` 🚀
2. When prompted, enter the directory path containing the PDF files to be renamed
3. The program will rename all the PDF files in the directory according to the format "Song name - Artist name" 🎶🎨

## Project Structure 📁

The project has the following files:

- `main.py`: This is the main file of the application. It is responsible for initiating the application and calling the necessary functions from other files.
- `musicbrainzapi.py`: This file contains the functions that interact with the MusicBrainz API. It exports a function that takes a song name as input and returns the correct song name and artist name by querying the MusicBrainz API.
- `requirements.txt`: This file lists the dependencies of the Python project. 📦

## Contributing 🤝

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License 📄

This project is licensed under the MIT License - see the LICENSE.md file for details 📝
