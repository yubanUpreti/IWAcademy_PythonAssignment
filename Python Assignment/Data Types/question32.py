def square_number(n):
	dic1 = {}
	for i in range(1,n):
		dic1[i] = i*i
	return dic1

print(square_number(10))