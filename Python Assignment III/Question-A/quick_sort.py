print("#"*50)
print("")
print("*"*20+"  Quick Sort  "+"*"*20)

random_numbers= [99,1,16,2,31]
x = random_numbers.copy()
def swap3(unsorted_list):
	if len(unsorted_list) <= 1:
		return unsorted_list
	lower,higher,value= [],[],unsorted_list.pop()
	for val in unsorted_list:
		if val <= value: lower.append(val)
		else: higher.append(val)
	return swap3(lower)+[value]+swap3(higher)

print(f" Before Quick Sort : {random_numbers} ")
print("")
print(f" After  Quick Sort : {swap3(x)} ")

print("")
print("#"*50)