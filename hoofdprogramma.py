from read_data_users import dict_user_data

users = dict_user_data()

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

login(users)