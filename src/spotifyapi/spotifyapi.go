package spotifyapi

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
)

type SpotifyResponse struct {
	Tracks struct {
		Items []struct {
			Name    string `json:"name"`
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

	spotifyKey := os.Getenv("SPOTIFY_KEY")
	if spotifyKey == "" {
		return "", "", fmt.Errorf("SPOTIFY_KEY environment variable is not set")
	}

	req, err := http.NewRequest("GET", baseURL, nil)
	if err != nil {
		return "", "", err
	}

	req.Header.Add("Authorization", fmt.Sprintf("Bearer %s", spotifyKey))
	req.URL.RawQuery = data.Encode()

	// Now you can send the request using http.Client
	client := &http.Client{}

	resp, err := client.Do(req)
	if err != nil {
		return "", "", fmt.Errorf("failed to send HTTP request: %w", err)
	}

	if err != nil {
		return "", "", err
	}
	defer resp.Body.Close()

	// Process the response here...

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", "", err
	}

	var spotifyResp SpotifyResponse
	err = json.Unmarshal(body, &spotifyResp)
	if err != nil {
		return "", "", fmt.Errorf("failed to parse response body: %w", err)
	}

	if len(spotifyResp.Tracks.Items) == 0 {
		return "", "", fmt.Errorf("no track found")
	}

	track := spotifyResp.Tracks.Items[0]
	artist := track.Artists[0].Name
	song := track.Name

	return song, artist, nil
}
