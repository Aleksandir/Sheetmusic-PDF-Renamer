package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
)

type Artist struct {
	ID       string `json:"id"`
	Name     string `json:"name"`
	SortName string `json:"sort-name"`
}

type ArtistCredit struct {
	Name   string `json:"name"`
	Artist struct {
		ID       string `json:"id"`
		Name     string `json:"name"`
		SortName string `json:"sort-name"`
	} `json:"artist"`
}

type Recording struct {
	ID           string         `json:"id"`
	Score        int            `json:"score"`
	StatusID     string         `json:"status-id"`
	PackagingID  string         `json:"packaging-id"`
	Count        int            `json:"count"`
	Title        string         `json:"title"`
	Status       string         `json:"status"`
	Packaging    string         `json:"packaging"`
	ArtistCredit []ArtistCredit `json:"artist-credit"`
}

type Response struct {
	ArtistCredit [0]ArtistCredit `json:"artist-credit"`
	Created      string          `json:"created"`
	Count        int             `json:"count"`
	Offset       int             `json:"offset"`
	Recordings   []Recording     `json:"recordings"`
}

func main() {
	// url for testing https://musicbrainz.org/ws/2/release?'limit=1&query=Chasing-Cars-Part&fmt=json
	song := "Chasing-Cars-Part" // replace with your song title
	resp, err := http.Get("https://musicbrainz.org/ws/2/release?'limit=1&query=" + url.QueryEscape(song) + "&fmt=json")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// this is to close the body after the function is done
	defer resp.Body.Close()

	// read the body of the response
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// unmarshal the json into a struct
	var recording Recording
	unmarshalErr := json.Unmarshal(body, &recording)
	if unmarshalErr != nil {
		fmt.Println("Error:", unmarshalErr)
		return
	}

	fmt.Println("Title:", recording.Title)
	if len(recording.ArtistCredit) > 0 {
		fmt.Println("Artist:", recording.ArtistCredit[0].Name)
	} else {
		fmt.Println("No artist credit found.")
	}

}
