add = input("add contact? Y/N\n").lower()

while add == "y":
  contact = input("contact name:\n")
  number = input("contact's number:\n")
  email = input("Email: ").strip()
  username = email[:email.index("@")]
  print(f"Contact name: {contact}\nNumber: {number}\nUsername: {username}")
  add = input("add contact? Y/N\n").lower()
  if add == "n":
    break
