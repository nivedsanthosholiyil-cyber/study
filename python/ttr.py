import re
url = input("enter a url: ").strip()
name = re.sub(r"^https?://(www\.)?", "", url)   