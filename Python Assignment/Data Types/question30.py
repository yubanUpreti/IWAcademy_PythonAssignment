dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

try:
	key = 2
	if dic1[key]:
		print("Key exist in the Dictionary Object")
except KeyError as e:
	print("Key '{}' not found in Dictionary Object".format(e))