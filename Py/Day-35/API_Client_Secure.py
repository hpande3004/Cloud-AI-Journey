import requests
import logging

from config import API_KEY, API_BASE_URL


logging.basicConfig(
    filename="api_client.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def handle_response(response):

    if response.status_code == 200:
        print("Request successful.")
        return True

    elif response.status_code == 201:
        print("Resource created successfully.")
        return True

    elif response.status_code == 204:
        print("Request successful. No content.")
        return True

    elif response.status_code == 400:
        print("Bad request.")

    elif response.status_code == 401:
        print("Unauthorized. Check your API credentials.")

    elif response.status_code == 403:
        print("Forbidden. You don't have permission.")

    elif response.status_code == 404:
        print("Resource not found.")

    elif response.status_code >= 500:
        print("Server error.")

    else:
        print(
            f"Unexpected status code: "
            f"{response.status_code}"
        )

    return False


def get_users(limit=5):

    url = f"{API_BASE_URL}/users"

    params = {
        "_limit": limit
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=HEADERS,
            timeout=10
        )

        logging.info(
            f"GET {response.url} → "
            f"{response.status_code}"
        )

        if not handle_response(response):
            return []

        return response.json()

    except requests.exceptions.Timeout:

        logging.error("GET request timed out.")

        print("Request timed out.")

    except requests.exceptions.RequestException as error:

        logging.error(
            f"GET request failed: {error}"
        )

        print(
            f"Request failed: {error}"
        )

    return []


def get_user_by_id(user_id):

    url = f"{API_BASE_URL}/users/{user_id}"

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        logging.info(
            f"GET USER {user_id} → "
            f"{response.status_code}"
        )

        if not handle_response(response):
            return None

        return response.json()

    except requests.exceptions.RequestException as error:

        logging.error(
            f"GET USER failed: {error}"
        )

        print(
            f"Request failed: {error}"
        )

    return None


def create_post():

    url = f"{API_BASE_URL}/posts"

    data = {
        "title": "Secure API Client",
        "body": "Learning API configuration.",
        "userId": 1
    }

    try:

        response = requests.post(
            url,
            json=data,
            headers=HEADERS,
            timeout=10
        )

        logging.info(
            f"POST {response.url} → "
            f"{response.status_code}"
        )

        if not handle_response(response):
            return None

        return response.json()

    except requests.exceptions.RequestException as error:

        logging.error(
            f"POST request failed: {error}"
        )

        print(
            f"Request failed: {error}"
        )

    return None


def main():

    print("==============================")
    print("     SECURE API CLIENT")
    print("==============================")

    users = get_users()

    if users:

        print("\nUsers")
        print("------------------------------")

        for user in users:

            print(
                f"{user['id']} - "
                f"{user['name']} - "
                f"{user['email']}"
            )

    print("\nTesting single user...")

    user = get_user_by_id(1)

    if user:

        print(
            f"User: {user['name']}"
        )

    print("\nTesting POST request...")

    post = create_post()

    if post:

        print(
            f"Created Post ID: "
            f"{post['id']}"
        )


if __name__ == "__main__":
    main()