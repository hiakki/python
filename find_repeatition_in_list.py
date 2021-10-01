list = ['a', 'b', 'c', 'd', 'c', 'b', 'a']

group = {}

for letter in list:
    if letter not in group.keys():
        group[letter] = 1
    else:
        group[letter]+=1

print(group)