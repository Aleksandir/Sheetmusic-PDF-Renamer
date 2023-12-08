# Spotify PDF Renamer

This project is a Go program that renames PDF files in a directory using the Spotify API. The program takes the existing file names, which are assumed to be song names, and queries the Spotify API to get the correct song name and artist name. The PDF files are then renamed to the format "Song name - Artist name".

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Go 1.16 or later
- A Spotify Developer account to get API credentials

### Installing

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Run `go mod tidy` to download the necessary dependencies

### Usage

1. Run the program with `go run src/main.go`
2. When prompted, enter the directory path containing the PDF files to be renamed
3. The program will rename all the PDF files in the directory according to the format "Song name - Artist name"

## Project Structure

The project has the following files:

- `src/main.go`: This is the main file of the application. It is responsible for initiating the application and calling the necessary functions from other files.
- `src/spotifyapi/spotifyapi.go`: This file contains the functions that interact with the Spotify API. It exports a function that takes a song name as input and returns the correct song name and artist name by querying the Spotify API.
- `src/filerename/filerename.go`: This file contains the functions for renaming the PDF files. It exports a function that takes a directory path and a function for renaming a file as input. It goes through each PDF file in the directory, uses the renaming function to get the new name, and renames the file.
- `go.mod` and `go.sum`: These files are used for managing the dependencies of the Go project. `go.mod` is used for declaring the module path and the dependency requirements. `go.sum` is used for ensuring the integrity of the dependencies.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details