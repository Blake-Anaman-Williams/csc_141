Colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']

print(Colors[0])

Colors[0] = 'Orange'
print(Colors[0])

Colors.insert(0, 'Tourquoise')
print(Colors[0])

Colors.append('White')
print(Colors)

Removed_color = Colors.pop()
print(Removed_color)
print(Colors)

del Colors[0]
print(Colors)

colors.sort()
print(Colors)

colors.reverse()
print(Colors)

colors.sort(reverse=True)
print(Colors)

print(len(Colors))