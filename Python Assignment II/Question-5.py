
# Tuple Manipulation 

my_information = ('Youban','Uprety','26')
friend_1_information = ('Sagar','Dahal','26')
friend_2_information = ('Niroj','Koirala','27')
friend_3_information = ('Pratik','Upadhaya','26')


people = []
print('')

people.append(my_information)
people.append(friend_1_information)
people.append(friend_2_information)
people.append(friend_3_information)

print("Data append to list")
print('')
sorted_people = sorted(people)

# Sorted by First Name
print('Sorted by First Name')
print('')
print(sorted_people)
print('')

# Sorted by Last Name
sorted_people = sorted(people,key= lambda x: x[1])

print('Sorted by Last Name')
print('')
print(sorted_people)
print('')
