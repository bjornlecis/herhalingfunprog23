import csv

import csv

users = {"Bjorn": "1234", "admin": "admin"}

csv_file_path = "users.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Username", "Password"])

    # Write data
    for user, password in users.items():
        writer.writerow([user, password])

