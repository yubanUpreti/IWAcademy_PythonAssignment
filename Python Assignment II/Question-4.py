
# List manipulation 

friends_list = []

print(id(friends_list))
print('')

friends_list.append("Sagar")
friends_list.append("Pratik")
friends_list.append("Niroj")

print("Data append to list")
print('')
print(id(friends_list))

# No the ID hasn't changed 

print(friends_list)
sorted_friends_list = sorted(friends_list)

print(sorted_friends_list)

# First item on sorted list

print(sorted_friends_list[0])

# Second item on sorted list

print(sorted_friends_list[1])