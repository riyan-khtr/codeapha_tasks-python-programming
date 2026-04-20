#  Web Title Scraper (Python)

##  Overview
This Python script connects to a webpage, reads its HTML content, extracts the text inside the `<title>` tag, and saves it to a text file. It demonstrates basic web scraping using simple tools without external parsers.

##  Objective
To automatically fetch and store the title of a fixed webpage.

##  Technologies & Concepts Used
- Python
- `requests` module (HTTP request)
- `re` module (regex for title extraction)
- File handling (write output to file)

##  Project Files
- `scrape_title.py` – Python script
- `web_title.txt` – Output file containing the webpage title

##  How to Run
1. Install dependency (once):
   ```bash
   pip install requests