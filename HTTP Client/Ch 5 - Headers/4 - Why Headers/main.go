package main

import "fmt"

func main() {
	url := "https://api.boot.dev/v1/courses_rest_api/learn-http/projects/52fdfc07-2182-454f-963f-5f0f9a621d72"
	apiKey := generateKey()

	oldProject, err := getProjectResponse(apiKey, url)
	if err != nil {
		fmt.Println("Error getting old project:", err)
		return
	}
	fmt.Println("Got old project:")
	fmt.Printf("- name: %s\n", oldProject.Name)
	fmt.Printf("- numUsers: %d\n", oldProject.NumUsers)
	fmt.Println("--------------------------------")

	newProjectData := Project{
		ID:        "52fdfc07-2182-454f-963f-5f0f9a621d72",
		Name:      "Product Roadmap 2025",
		Completed: false,
		NumUsers:  1,
	}

	if err := putProject(apiKey, url, newProjectData); err != nil {
		fmt.Println("Error updating project:", err)
		return
	}
	fmt.Println("Project updated!")
	fmt.Println("---")

	// newApiKey := generateKey()
	newProject, err := getProjectResponse(apiKey, url)
	if err != nil {
		fmt.Println("Error getting new project:", err)
		return
	}
	fmt.Println("Got new project:")
	fmt.Printf("- name: %s\n", newProject.Name)
	fmt.Printf("- numUsers: %d\n", newProject.NumUsers)
	fmt.Println("--------------------------------")
}
