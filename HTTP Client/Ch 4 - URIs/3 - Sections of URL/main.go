package main

import "net/url"

func newParsedURL(urlString string) ParsedURL {
	parsedURL, err := url.Parse(urlString)
	if err != nil {
		return ParsedURL{}
	}

	protocol := parsedURL.Scheme
	username := parsedURL.User.Username()
	password, _ := parsedURL.User.Password()
	hostname := parsedURL.Hostname()
	port := parsedURL.Port()
	path := parsedURL.Path
	search := parsedURL.RawQuery
	hash := parsedURL.Fragment

	return ParsedURL{
		protocol: protocol,
		username: username,
		password: password,
		hostname: hostname,
		port:     port,
		pathname: path,
		search:   search,
		hash:     hash,
	}
}
