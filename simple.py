
print("===== LOGIN PAGE =====")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    print("Login Successful!")
    print("Welcome", username)
else:
    print("Invalid Username or Password")
