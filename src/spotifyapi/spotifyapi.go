package spotifyapi

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

type SpotifyResponse struct {
	Tracks struct {
		Items []struct {
			Name   string `json:"name"`
			Artists []struct {
				Name string `json:"name"`
			} `json:"artists"`
		} `json:"items"`
	} `json:"tracks"`
}

func GetSongAndArtist(songName string) (string, string, error) {
	baseURL := "https://api.spotify.com/v1/search"
	data := url.Values{}
	data.Set("q", songName)
	data.Set("type", "track")
	data.Set("limit", "1")

	req, err := http.NewRequest("GET", baseURL+"?"+data.Encode(), nil)
	if err != nil {
		return "", "", err
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", "", err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", "", err
	}

	var spotifyResp SpotifyResponse
	err = json.Unmarshal(body, &spotifyResp)
	if err != nil {
		return "", "", err
	}

	if len(spotifyResp.Tracks.Items) == 0 {
		return "", "", fmt.Errorf("no track found")
	}

	track := spotifyResp.Tracks.Items[0]
	artist := track.Artists[0].Name
	song := track.Name

	return song, artist, nil
}