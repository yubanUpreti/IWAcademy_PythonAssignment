print("#"*50)
print("")
print("*"*20+"  Merge Sort  "+"*"*20)

def divide_and_conqure(array):

	if(len(array) <= 1):
		return array
	else:
		return merge_sort(left_sorted_seq= divide_and_conqure(array[0:((len(array) // 2))]), right_sorted_seq=divide_and_conqure(array[((len(array) // 2)):]))

def merge_sort(left_sorted_seq, right_sorted_seq):
	left_i,right_i,merged = 0,0,[]
	left_sorted_len,right_sorted_len = len(left_sorted_seq),len(right_sorted_seq)
	append = merged.append

	while left_i < left_sorted_len and right_i < right_sorted_len:
	    smallestInLeft = left_sorted_seq[left_i]
	    smallestInRight = right_sorted_seq[right_i]

	    if smallestInLeft < smallestInRight:
	        append(smallestInLeft)
	        left_i += 1
	    else:
	        append(smallestInRight)
	        right_i += 1

	if left_i < left_sorted_len:
	    return [*merged , *left_sorted_seq[left_i:]]
	return [*merged , *right_sorted_seq[right_i:]]

random_numbers= [99,1,16,2,31]
x= random_numbers.copy()

print(f" Before Merge Sort : {random_numbers} ")
print("")
print(f" After  Merge Sort : {divide_and_conqure(x)} ")


print("")
print("#"*50)