import re
emal = input("Enter your email address: ").strip()

if re.search(r"^\w+@\w+\.edu$", emal):
    print("Valid email address")
else:
    print("Invalid email address")