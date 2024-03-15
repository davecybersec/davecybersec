'''
Copyright (C) 2023
Password Breach Detection
Author: David Probert
'''

import requests
import hashlib
import csv

# Define the name of the CSV file
csv_file = "<add the path to your file here>"

# Define the name of the password column within the csv file
password_col = "password"

# Define the URL for the HaveIBeenPwned API
pwned_api_url = "https://api.pwnedpasswords.com/range/"

# Open the CSV file and create a CSV reader object
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)

    # Loop through each row in the CSV file
    for row in reader:
        # Get the password from the password column
        password = row[password_col]

        # Hash the password using SHA-1
        password_hash = hashlib.sha1(str(password).encode("utf-8")).hexdigest().upper()

        # Send a GET request to the HaveIBeenPwned API to check if the password has been breached
        response = requests.get(pwned_api_url + password_hash[:5])

        # If the API returns a 200 status code, check if the password hash appears in the response body
        if response.status_code == 200:
            for line in response.text.splitlines():
                if password_hash[5:] in line:
                    print(f"The password {password} has been breached {line.split(':')[1]} times.")
                    break
        else:
            print("An error occurred while checking the password with HaveIBeenPwned.")
