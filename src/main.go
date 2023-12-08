package main

import (
	"log"
	"os"
	"path/filepath"
	"strings"

	"spotifyapi"

	"github.com/aleksandir/filerenamer/src/filerename/filerename.go"
	"github.com/aleksandir/filerenamer/src/spotifyapi/spotifyapi.go"
)

func main() {
	// Get the directory path from the command line arguments
	dirPath := os.Args[1]

	// Get all PDF files in the directory
	pdfFiles, err := filepath.Glob(filepath.Join(dirPath, "*.pdf"))
	if err != nil {
		log.Fatal(err)
	}

	// For each PDF file
	for _, oldPath := range pdfFiles {
		// Get the old name without the extension
		oldName := strings.TrimSuffix(filepath.Base(oldPath), filepath.Ext(oldPath))

		// Get the correct song name and artist name from the Spotify API
		newName, err := spotifyapi.GetSongAndArtist(oldName)
		if err != nil {
			log.Println("Error getting song and artist:", err)
			continue
		}

		// Get the new path
		newPath := filepath.Join(filepath.Dir(oldPath), newName+".pdf")

		// Rename the file
		err = filerename.Rename(oldPath, newPath)
		if err != nil {
			log.Println("Error renaming file:", err)
			continue
		}

		log.Println("Renamed", oldPath, "to", newPath)
	}
}
