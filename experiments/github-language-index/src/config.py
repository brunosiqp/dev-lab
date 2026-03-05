import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

BASE_URL = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

SEARCH_QUERY = "stars:>10 created:>2024-01-01"
PER_PAGE = 100
MAX_PAGES = 10  # adjust as needed
OUTPUT_DIR = "output"