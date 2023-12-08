package main

import (
	"encoding/base64"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"strings"

	"github.com/joho/godotenv"
)

func main() {
	// Load .env file
	err := godotenv.Load("src/.env")
	if err != nil {
		fmt.Println("Error loading .env file")
		return
	}

	clientID := os.Getenv("SPOTIFY_CLIENT_ID")
	clientSecret := os.Getenv("SPOTIFY_CLIENT_SECRET")

	// Base64 encode the client ID and secret
	auth := base64.StdEncoding.EncodeToString([]byte(clientID + ":" + clientSecret))

	data := url.Values{}
	data.Set("grant_type", "client_credentials")

	req, err := http.NewRequest("POST", "", strings.NewReader(data.Encode()))
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	req.Header.Add("Authorization", "Basic "+auth)
	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	// handle response
	fmt.Println("Response:", string(resp.Status))
}

// func getToken() string {
// 	authString := fmt.Sprintf("%v:%v", os.Getenv("CLIENT_ID"), os.Getenv("CLIENT_SECRET"))
// 	encodedAuthString := base64.StdEncoding.EncodeToString([]byte(authString))

// 	return encodedAuthString
// }
