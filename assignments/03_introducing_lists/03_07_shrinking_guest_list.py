celebrities= ['Kobe', 'Walker','Messi']
print("Dear", celebrities[0], 'I would like to invite you to Dinner.')
print("Dear", celebrities[1], 'I would like to invite you to Dinner.')
print("Dear", celebrities[2], 'I would like to invite you to Dinner.')   

print(celebrities[0],"Is unable to attend the dinner.")

celebrities[0] = "Ronaldo"
print("Dear", celebrities[0], 'I would like to invite you to Dinner.')
print("Dear", celebrities[1], 'I would like to invite you to Dinner.')
print("Dear", celebrities[2], 'I would like to invite you到 Dinner.') 

print('I have found a bigger dinner table.')

celebrities.insert(0, "Elon")
celebrities.insert(2, "Curry")
celebrities.append("Chris") 

print("Only two people can come to dinner.")

Removed_guest = celebrities.pop()
print("Dear", Removed_guest, 'I am sorry to inform you that I can not invite you to dinner.')

Removed_guest_1 = celebrities.pop()
print("Dear", Removed_guest_1, 'I am sorry to inform you that I can not invite you to dinner.')

Removed_guest_2 = celebrities.pop()
print("Dear", Removed_guest_2, 'I am sorry to inform you that I cannot invite you to dinner.')

Removed_guest_3 = celebrities.pop()
print("Dear", Removed_guest_3, 'I am sorry to inform you that I cannot invite you to dinner.')

print("Dear", celebrities[0], 'You are still invited to dinner.')
print("Dear", celebrities[1], 'You are still invited to dinner.')

del celebrities[1]
del celebrities[0]
print(celebrities)
