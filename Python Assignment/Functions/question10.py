sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_from_list(sample_list):
	return list(filter(None, ([x if x%2==0 else ''  for x in sample_list])))


print(even_from_list(sample_list))

