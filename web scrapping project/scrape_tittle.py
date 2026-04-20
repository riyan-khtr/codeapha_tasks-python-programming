import requests
import re

URL = "https://www.geeksforgeeks.org"
OUTPUT_FILE = "web_title.txt"

def scrape_title():
    response = requests.get(URL)
    html = response.text

    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    title = match.group(1) if match else "No title found"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(title)

    print("Webpage title saved to web_title.txt")

if __name__ == "__main__":
    scrape_title()