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
	Artist Artist `json:"artist"`
}

type Recording struct {
	ID               string         `json:"id"`
	Score            int            `json:"score"`
	Title            string         `json:"title"`
	Length           int            `json:"length"`
	ArtistCredit     []ArtistCredit `json:"artist-credit"`
	FirstReleaseDate string         `json:"first-release-date"`
	Video            interface{}    `json:"video"` // Use interface{} if the type is unknown
	Isrcs            []string       `json:"isrcs"`
	Disambiguation   string         `json:"disambiguation"`
}

type Response struct {
	Created    string      `json:"created"`
	Count      int         `json:"count"`
	Offset     int         `json:"offset"`
	Recordings []Recording `json:"recordings"`
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
	var response Response
	err = json.Unmarshal(body, &response)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	formattedJSON, err := json.MarshalIndent(response, "", "  ")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println(string(formattedJSON))

	if len(response.Recordings) > 0 {
		firstRecording := response.Recordings[0]
		fmt.Println("First track name:", firstRecording.Title)
		if len(firstRecording.ArtistCredit) > 0 {
			fmt.Println("First artist:", firstRecording.ArtistCredit[0].Name)
		} else {
			fmt.Println("No artist credit found.")
		}
	} else {
		fmt.Println("No recordings found.")
	}
}
