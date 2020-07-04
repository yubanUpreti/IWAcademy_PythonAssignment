


random_list = [1,9,6,5,2,47]


def binary_search(search_value,start,end,arg_list):

	if end >= start:
		middle = (start + end) // 2
		if search_value == arg_list[middle]:
			return arg_list.index(search_value)
			# return middle
		elif arg_list[middle] > search_value:
			return binary_search(search_value,start,middle-1,arg_list)
		else:
			return binary_search(search_value,middle+1,end,arg_list)
	else:
		return -1



print(binary_search(6,0,len(random_list)-1,sorted(random_list)))