
""" Blake Anaman-Wiiliams
This is my work 
This program checks if there are any users in the list and 
prints out a message depending on the result.
"""


usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello, " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")