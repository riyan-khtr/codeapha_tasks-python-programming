import re

INPUT_FILE = "input.txt"      # your source file
OUTPUT_FILE = "emails.txt"   # where emails will be saved

def extract_emails(text):
    # Regex for matching emails
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'
    return re.findall(pattern, text)

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    emails = extract_emails(content)
    unique_emails = sorted(set(emails))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print(f"Found {len(unique_emails)} unique emails.")
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()