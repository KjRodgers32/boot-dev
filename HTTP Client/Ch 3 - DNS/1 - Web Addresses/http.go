package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
)

func getIPAddress(domain string) (string, error) {
	url := fmt.Sprintf("https://cloudflare-dns.com/dns-query?name=%s&type=A", domain)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return "", fmt.Errorf("error creating request: %w", err)
	}
	req.Header.Set("accept", "application/dns-json")

	client := http.Client{}
	res, err := client.Do(req)
	if err != nil {
		return "", fmt.Errorf("error sending request: %w", err)
	}
	defer res.Body.Close()

	var dnsres DNSResponse

	decoder := json.NewDecoder(res.Body)
	if err = decoder.Decode(&dnsres); err != nil {
		return "", err
	}

	if dnsres.Answer[0].Data == "" {
		return "", errors.New("new values")
	}

	return dnsres.Answer[0].Data, nil
}

func main() {
	domain := "boot.dev"
	getIPAddress(domain)
}
