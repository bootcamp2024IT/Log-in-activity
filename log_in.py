users = {}

def register():
    write = open("storage.txt", "a")
    username = input("Username: ")
    if username in users:
        print(f"{username} is already taken as a username")
    else:
        password = input("Password: ")
        users[username] = password
        print(f"Username:{username}  Password:{users[username]}", file=write)
        print(f"User {username} has been created")    
        write.close()

def log_in():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and password in users[username]:
        print(f"You have successfully logged in as {username}")
    else:
        print("Login Failed") 

def change_pass():
    write = open("storage.txt", "a")
    username = input("Username: ")
    password = input("Enter old password: ")
    if username in users and password in users[username]:
        new_password = input("Enter new password: ")
        users[username] = new_password
        print(f"Username:{username} Password:{users[username]}", file=write)
        print(f"Password for {username} has been changed!")
        write.close()
    else:
        print("User not found or Incorrect password")    

while True:
    print('''Welcome
          1. Login
          2. Register
          3. Change Password''')

    choice = int(input("What to do? "))

    if choice == 1:
        log_in()
    elif choice == 2:
        register()       
    elif choice == 3:
        change_pass() 
    else:
        print("Choose properly")