""" Blake Anaman-Wiiliams
This is my work 
This program checks the username of a person and 
prints out a message depending on the username.
"""



usernames = ['admin', 'Jaden', 'Blake', 'Byshir', 'David']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello, " + username + ", thank you for logging in again.")