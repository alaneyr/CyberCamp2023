import requests
# Prompt the user for destination URL
url = input("https://github.com/alaneyr")
# Prompt the user to select an HTTP Method
http_method = input("Choose an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
# Display the request details to the user
print(f"\nSending a {http_method} request to: {url}")
# Confirm with the user before proceeding
confirmation = input("Do you want to proceed? (yes/no): ").lower()
if confirmation != 'yes':
    print("Request canceled.")
else:
    # Perform the HTTP request
    if http_method == 'GET':
        response = requests.get(url)
    elif http_method == 'POST':
        response = requests.post(url)
    elif http_method == 'PUT':
        response = requests.put(url)
    elif http_method == 'DELETE':
        response = requests.delete(url)
    elif http_method == 'HEAD':
        response = requests.head(url)
    elif http_method == 'PATCH':
        response = requests.patch(url)
    elif http_method == 'OPTIONS':
        response = requests.options(url)
    else:
        print("Invalid HTTP Method. Exiting.")
        exit()
    # Print response details
    print(f"\nResponse Status Code: {response.status_code}")
    # Translate status code into plain terms
    if response.status_code == 404:
        print("Site not found")
    elif response.status_code == 200:
        print("Request successful")
    # Add more status code translations as needed
    # Print response headers
    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")