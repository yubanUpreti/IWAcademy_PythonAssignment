
# Find in List 




friends = ['Niroj', 'Pratik', 'Sagar','John','Youban']
print('')



for name in friends:
	if 'john' in name.lower():
		print(f"\'John\' Name Found at position {friends.index('John')}")
	else:
		print("\'John\' Name Not Found")

