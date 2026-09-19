import re
url = input("enter a url: ").strip()
matches = re.search(r"^https?://(www\.)?(\w+)\.(\w+)$", url)
if matches:
    print(f"Valid url: {matches.group(2)}")