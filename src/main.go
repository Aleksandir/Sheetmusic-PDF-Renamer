package main

import (
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/aleksandir/Sheetmusic-renamer/src/spotifyapi"
)

func main() {
	// Get the directory path from the command line arguments
	// dirPath := os.Args[1]
	//! for testing
	dirPath := "testFiles"

	// Get all PDF files in the directory
	pdfFiles, err := filepath.Glob(filepath.Join(dirPath, "*.pdf"))
	if err != nil {
		log.Fatal(err)
	}

	// For each PDF file
	for _, oldPath := range pdfFiles {
		// Get the old name without the extension
		oldName := strings.TrimSuffix(filepath.Base(oldPath), filepath.Ext(oldPath))

		newName, _, err := spotifyapi.GetSongAndArtist(oldName)
		if err != nil {
			log.Println("Error getting song and artist:", err)
			continue
		}

		// Get the new path
		newPath := filepath.Join(filepath.Dir(oldPath), newName+".pdf")

		err = os.Rename(oldPath, newPath)
		if err != nil {
			log.Println("Error renaming file:", err)
			continue
		}

		log.Println("Renamed", oldPath, "to", newPath)
	}
}
