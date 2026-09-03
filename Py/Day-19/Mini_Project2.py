'''API Data Fetcher Mini Project'''

import requests

post_id = input("Post ID: ")


try:
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}", timeout = 5)
    response.raise_for_status()                      # Raise an exception for HTTP errors
    data = response.json()
    print("\n------POST DETAILS------")
    print("\nUser ID:", data['userId'])
    print("Post ID:", data['id'])
    print("Title:", data['title'])
    print("Body:", data['body'])
except requests.exceptions.HTTPError as http_err:
    print("API failed request", http_err)