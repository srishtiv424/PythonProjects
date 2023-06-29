def view():
    with open("password.txt", "r") as pwd:
        for line in pwd.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User : {user}   Password : {passw}")


def add():
    username = input("Enter the username")
    password = input("Enter the password")
    with open("password.txt", "a") as pwd:
        pwd.write(f"Username: {username} | Password: {password}")
    print("Successfully Added !!")


while True:
    print("Welcome to your Password Manager")
    master_pass = input("Enter your password")
    choice = input("Are you here to \n 1. View \n 2. Add \n").lower()
    if choice == "q":
        break
    if choice == "view":
        view()
    elif choice == "add":
        add()
    else:
        print("Wrong Choice")
