
# Fetch GitHub User Details


## What Does the Code Do?
This Python script fetches details of a GitHub user using the GitHub API. It takes a GitHub username as input and retrieves information such as the user's name and the number of public repositories they have.

## Why Use This Code?
- To programmatically retrieve GitHub user details for automation or integration into other applications.
- To demonstrate how to interact with REST APIs and handle JSON responses in Python.

## How Does It Work?
1. **Input**: The script takes a GitHub username as a command-line argument.
2. **API Request**: It sends a GET request to the GitHub API endpoint (`https://api.github.com/users/{username}`).
3. **Error Handling**: The `response.raise_for_status()` method ensures the request was successful (status code 200) and raises an error for unsuccessful requests.
4. **JSON Parsing**: The response is parsed into a Python dictionary using `response.json()`.
5. **Output**: The script prints the user's name and the number of public repositories.

## Example Usage
Run the script from the command line:
```bash
python script.py <username>
```

Replace `<username>` with the GitHub username you want to fetch details for.

