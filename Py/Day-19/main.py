import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response)

data  = response.json()

print(data)
print(data['title'])
print(data['body'])

# ------------------------------------
#Status Code: 200 (OK)

import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status Code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print("\nUser ID:", data['userId'])
    print("Post ID:", data['id'])
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Something went wrong. Status Code:", response.status_code)

# -------------------------------------
#Status Code: 404 (Not Found)

import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/999999")
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Something went wrong. Status Code:", response.status_code)

# --------------------------------------
# Proper API error handling

import requests
try:
    response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/999999",
    timeout = 5                                      # Set a timeout for the request
    )

    response.raise_for_status()                      # Raise an exception for HTTP errors
    data = response.json()
    print("\nUser ID:", data['userId'])
    print("Post ID:", data['id'])
    print("Title:", data['title'])
    print("Body:", data['body'])
except requests.exceptions.HTTPError as http_err:
    print("API failed request", http_err)