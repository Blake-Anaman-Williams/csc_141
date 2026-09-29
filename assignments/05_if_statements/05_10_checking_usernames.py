""" Blake Anaman-Wiiliams
This is my work 
And this was really confusing
"""



current_users = ['Brian', 'Jaden', 'Blake', 'Adam', 'David']

new_users = ['brian', 'Alex', 'John', 'BLAKE', 'Kevin']

current_users_lower = ['brian', 'jaden', 'blake', 'adam', 'david']

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("The username " + new_user + " will need to enter a new username.")
    else:
        print("The username " + new_user + " is available.")