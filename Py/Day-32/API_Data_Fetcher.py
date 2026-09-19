import requests
import json
import logging


API_URL = "https://jsonplaceholder.typicode.com/users"

OUTPUT_FILE = "users.json"


# Configure logging
logging.basicConfig(
    filename="api_fetcher.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_users():
    try:
        response = requests.get(API_URL, timeout=10)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        users = response.json()
        print(type(users[0]))

        logging.info(
            f"Successfully fetched {len(users)} users."
        )

        return users

    except requests.exceptions.Timeout:
        logging.error("API request timed out.")
        print("Error: API request timed out.")

    except requests.exceptions.RequestException as error:
        logging.error(f"API request failed: {error}")
        print(f"API request failed: {error}")

    return []


def display_users(users):
    print("\nUsers")
    print("-----------------------------")

    for user in users:
        print(
            f"ID: {user['id']} | "
            f"Name: {user['name']} | "
            f"Email: {user['email']}"
        )


def filter_users(users):
    return [
        user
        for user in users
        if user["id"] > 5
    ]


def save_users(users):
    try:
        with open(
            OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                users,
                file,
                indent=4
            )

        logging.info(
            f"Saved {len(users)} users to {OUTPUT_FILE}"
        )

        print(
            f"\nSaved {len(users)} users "
            f"to {OUTPUT_FILE}"
        )

    except Exception as error:
        logging.error(
            f"Failed to save JSON: {error}"
        )

        print(
            f"Error saving JSON: {error}"
        )


def main():

    print("API Data Fetcher")
    print("================")

    users = fetch_users()

    if not users:
        print("No data received.")
        return

    print(
        f"\nSuccessfully fetched "
        f"{len(users)} users."
    )

    display_users(users)

    filtered_users = filter_users(users)

    print(
        f"\nFiltered users: "
        f"{len(filtered_users)}"
    )

    save_users(filtered_users)


if __name__ == "__main__":
    main()