items_in_list_one = [1, 3, 5, 7, 9, 10]
items_in_list_two = [2, 4, 6, 8]
new_list = items_in_list_one.copy()
new_list.pop(len(new_list)-1)
for val in items_in_list_two:
	new_list.append(val)


print(new_list)
