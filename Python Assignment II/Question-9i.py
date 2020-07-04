
# random_list = [1,9,6,5,2,47]


# def binary_search(search_value,arg_list):
# 	print(arg_list)
# 	print(arg_list[int(len(arg_list)/2)])
# 	if len(arg_list) == 1 and search_value != arg_list[0]:	
# 		return -1
# 	else:
# 		if search_value > arg_list[int(len(arg_list)/2)] and len(arg_list) != 1:
# 			new_list = arg_list[int(len(arg_list)/2):]
# 			print(int(len(arg_list)/2))
# 			print(new_list)
# 			if len(new_list) == 1 and search_value != new_list[0]:
# 				return -1
# 			else:
# 				if search_value > new_list[int(len(new_list)/2)]:
# 					return new_list.index(new_list[0])


# binary_search(5,sorted(random_list))


def binary_search(sorted_list, value,unsorted_list):
	middle = len(sorted_list)//2
	if(len(sorted_list)==1 and sorted_list[:]!=value):
		return -1
	else:
		if(sorted_list[middle]==value):
			return unsorted_list.index(value)
		elif(sorted_list[middle]>value):
			return binary_search(sorted_list[:middle], value,unsorted_list)
		elif(v>sorted_list[middle]):
			return binary_search(sorted_list[middle:], value,unsorted_list)

sample_list = [12,2,4,6,7,3,9,0,10,11,15,16,19]
# sample_list = [12,5]

print(binary_search(sorted(sample_list),12,sample_list))