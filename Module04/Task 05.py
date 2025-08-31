username = "python"
password = "rules"
attempts = 0

while attempts < 5:
    username1 = input("Enter a username: ")
    password1 = input("Enter a password: ")

    if username1 == username and password1 == password:
        print("Welcome ")
        break
    else:
        print("Wrong username or password")
        attempts += 1

if attempts == 5:
    print("Access Denied")