sample_list = [8,2,3,-1,7]

def multiply_list(sample_list):
	output = 1
	for value in sample_list:
		output *= value
	return output


print(multiply_list(sample_list))