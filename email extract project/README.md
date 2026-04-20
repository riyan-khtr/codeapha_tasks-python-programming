#  Email Extractor Automation Script

##  Overview
This Python script automates the process of finding and extracting email addresses from a text file. It reads the content of a file, detects valid email patterns using regular expressions (regex), and saves the extracted emails into a separate output file.

##  Objective
To reduce manual effort by automatically collecting email addresses from large text data.

## Technologies & Concepts Used
- Python
- Regular Expressions (re module)
- File Handling (read/write files)

##  Project Files
- `extract_emails.py` – Python script to extract emails
- `input.txt` – Text file containing content with emails
- `emails.txt` – Output file with extracted emails

##  How to Run
1. Place your text content with emails inside `input.txt`.
2. Open terminal in the project directory and run:
   ```bash
   python extract_emails.py