email = input("Enter your email address: ").strip()
usname, domain = email.split('@')
if usname and "." in domain 
    print("Valid email address.")
else:
    print("Invalid email address.")
