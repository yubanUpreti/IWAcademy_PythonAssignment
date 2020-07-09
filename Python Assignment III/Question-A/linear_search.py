print("")
print("#"*50)

print("#"*50)
print("")
print("*"*20+"  Linear Search  "+"*"*20)

random_numbers= [99,1,16,2,31]
search_value = 16

value = [ x if x==search_value else 0 for x in random_numbers ]
if not any(value):
	print(f"Data {search_value} not in list")
else:
	print(f"Data {search_value} in list at index {value.index(search_value)}")






print("")
print("#"*50)