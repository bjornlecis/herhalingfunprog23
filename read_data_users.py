import csv

csv_file_path = "users.csv"

users = {}

with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)

    # Skip the header
    header = next(reader)

    # Read data and populate the dictionary
    for row in reader:
        user, password = row
        users[user] = password

# Display the read data
"""print("Users read from CSV:")
for user, password in users.items():
    print(f"{user}: {password}")"""

def dict_user_data():
    return users