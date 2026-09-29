colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']

print(colors[0])

colors[0] = 'Orange'
print(colors[0])

colors.insert(0, 'Tourquoise')
print(colors[0])

colors.append('White')
print(colors)

Removed_color = colors.pop()
print(Removed_color)
print(colors)

del colors[0]
print(colors)

colors.sort()
print(colors)

colors.reverse()
print(colors)

colors.sort(reverse=True)
print(colors)

print(len(colors))