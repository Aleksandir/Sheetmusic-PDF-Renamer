# Sheetmusic PDF Renamer 🎵

This project is a Python program that renames sheet music PDF files in a directory using the Last.fm API. The program takes the existing file names, which are assumed to be song names, and queries the Last.fm API to get the correct song name and artist name. The PDF files are then renamed to the format "Song name - Artist name" 🎶🎨

Note: It is recommended that the file names already contain the song name and artist/composer to ensure accurate renaming. If the song name is shared with another artist's song, the program will default to the song with the most plays on Last.fm.

## Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋

- Python 3.7 or later (found [here](https://www.python.org/downloads/)) 🐍
- A Last.fm account to get API credentials 🔑

### Getting the API Key 🔑

To use the Last.fm API, you need to obtain an API key. Follow these steps to get your API key:

1. Visit the Last.fm API website at [https://www.last.fm/api/account/create](https://www.last.fm/api/account/create)
2. Sign in to your Last.fm account or create a new one if you don't have an account yet.
3. Once you have created an account, go to the API Keys section [here](https://www.last.fm/api/account/create) and follow the prompts.
4. Generate a new API key by clicking on the "Create an API account" button.
5. Copy the generated API key.

### Adding the API Key to the Program 🗝️

To use your API key in the program, follow these steps:

1. Open the `.env` file in a text editor
2. Locate the line that says `API_KEY = "YOUR_API_KEY_HERE"`.
3. Replace `"YOUR_API_KEY_HERE"` with your actual API key
4. Save the `.env` file.

## Installing 💻

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Install the necessary dependencies by running `pip install -r requirements.txt` 📦

### Usage 🎯

1. Run the program with `python main.py` 🚀
2. When prompted, enter the directory path containing the PDF files to be renamed
3. Check the proposed changes and select option 2 to ignore select files using the file numbers
4. The program will rename all the PDF files in the directory according to the format "Song name - Artist name" 🎶🎨

## Project Structure 📁

The project has the following files:

- `main.py`: This is the main file of the application. It is responsible for initiating the application and calling the necessary functions from other files.
- `lastfm.py`: This file contains the functions that interact with the Last.fm API. It exports a function that takes a song name as input and returns the correct song name and artist name by querying the Last.fm API.
- `requirements.txt`: This file lists the dependencies of the Python project. 📦

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details
