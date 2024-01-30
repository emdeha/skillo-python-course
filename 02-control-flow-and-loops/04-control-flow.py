username = "asdf"
password = "guest"

if username == "admin":
    if password == "password":
        print("Login successful! Welcome, admin.")
    elif password == "12345":
        print("Weak password. Please reset your password.")
    else:
        print("Incorrect password. Please try again.")
else:
    if username == "guest":
        if password == "guest":
            print("Login successful! Welcome, guest.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Unknown user. Please try again.")