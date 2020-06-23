def find_max(value1,value2,value3):
	if value1 > value2 and value1 > value3:
		return value1
	elif value2 > value1  and value2 > value3:
		return value2
	else:
		return value3


print(find_max(10,6,2))