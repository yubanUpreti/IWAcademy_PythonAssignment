print("#"*50)
print("*"*20+"  Binary Search  "+"*"*20)
print("")




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

random_numbers = [99,1,16,2,31]
search_value = 2
index_value = binary_search(search_value,0,len(random_numbers)-1,sorted(random_numbers))

print(f" The index of {search_value} is {index_value}")

print("")
print("#"*50)