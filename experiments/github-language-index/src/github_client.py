import requests
import time
from .config import BASE_URL, HEADERS, SEARCH_QUERY, PER_PAGE, MAX_PAGES


def fetch_repositories():
    repositories = []

    for page in range(1, MAX_PAGES + 1):
        url = f"{BASE_URL}/search/repositories"
        params = {
            "q": SEARCH_QUERY,
            "per_page": PER_PAGE,
            "page": page,
        }

        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code != 200:
            print(f"Error on page {page}: {response.status_code}")
            break

        data = response.json()
        items = data.get("items", [])

        if not items:
            break

        repositories.extend(items)
        print(f"Fetched page {page} ({len(items)} repos)")

        time.sleep(1)  # avoid rate limit

    return repositories