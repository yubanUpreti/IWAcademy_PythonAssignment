items_in_list = ['abc', 'xyz', 'aba', '1221']

count=0
for value in items_in_list:
	if len(value) > 2:
		if value[0]==value[-1]:
			count+=1
	else:
		continue

print(count)
