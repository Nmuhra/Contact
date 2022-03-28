contact = input("contact name:\n")
number = input("contact's number:\n")
email = input("Email: ").strip()
username = email[:email.index("@")]
print(f"Contact name: {contact}\nNumber: {number}\nUsername: {username}")
