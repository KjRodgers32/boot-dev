package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

func getIssues(url string) ([]Issue, error) {
	res, err := http.Get(url)
	if err != nil {
		return nil, fmt.Errorf("error creating request: %w", err)
	}

	defer res.Body.Close()
	var issues []Issue

	data, err := io.ReadAll(res.Body)
	if err != nil {
		return nil, fmt.Errorf("error parsing result data: %w", err)
	}

	if err = json.Unmarshal(data, &issues); err != nil {
		return nil, err
	}
	return issues, nil 
}