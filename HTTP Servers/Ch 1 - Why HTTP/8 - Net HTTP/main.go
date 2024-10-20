package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
)

const issueUrl = "https://api.boot.dev/v1/courses_rest_api/learn-http/issues"

func main() {
	issues, err := getIssueData(issueUrl)
	if err != nil {
		log.Fatalf("error getting issue data: %v", err)
	}

	prettyData, err := prettify(string(issues))
	if err != nil {
		log.Fatalf("error prettifying data: %v", err)
	}
	fmt.Println(prettyData)
}

func prettify(data string) (string, error) {
	var prettyJSON bytes.Buffer
	err := json.Indent(&prettyJSON, []byte(data), "", "	")
	if err != nil {
		return "", fmt.Errorf("error indenting JSON: %w", err)
	}
	return prettyJSON.String(), nil
}