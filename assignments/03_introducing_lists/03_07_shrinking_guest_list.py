Celebrities= ['Kobe', 'Walker','Messi']
print("Dear", Celebrities[0], 'I would like to invite you to Dinner.')
print("Dear", Celebrities[1], 'I would like to invite you to Dinner.')
print("Dear", Celebrities[2], 'I would like to invite you to Dinner.')   

print(Celebrities[0],"Is unable to attend the dinner.")

Celebrities[0] = "Ronaldo"
print("Dear", Celebrities[0], 'I would like to invite you to Dinner.')
print("Dear", Celebrities[1], 'I would like to invite you to Dinner.')
print("Dear", Celebrities[2], 'I would like to invite you to Dinner.')

print('I have found a bigger dinner table.')

Celebrities.insert(0, "Elon")
Celebrities.insert(2, "Curry")
Celebrities.append("Chris")

print("Only two people can come to dinner.")

Removed_guest = Celebrities.pop()
print("Dear", Removed_guest, 'I am sorry to inform you that I can not invite you to dinner.')

Removed_guest_1 = Celebrities.pop()
print("Dear", Removed_guest_1, 'I am sorry to inform you that I can not invite you to dinner.')

Removed_guest_2 = Celebrities.pop()
print("Dear", Removed_guest_2, 'I am sorry to inform you that I cannot invite you to dinner.')

Removed_guest_3 = Celebrities.pop()
print("Dear", Removed_guest_3, 'I am sorry to inform you that I cannot invite you to dinner.')

print("Dear", Celebrities[0], 'You are still invited to dinner.')
print("Dear", Celebrities[1], 'You are still invited to dinner.')

del Celebrities[1]
del Celebrities[0]
print(Celebrities)
