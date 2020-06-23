check = lambda x,y: True if x<y else False


def sort_using_lambda(sample_list):
	for j in range(len(sample_list)):
		for i in range(j,len(sample_list)):
			if check(sample_list[j],sample_list[i]) == True:
				continue
			else:
				temp = sample_list[j]
				sample_list[j] = sample_list[i]
				sample_list[i] = temp

sample_list = [1,5,2,9]

sort_using_lambda(sample_list)
print(sample_list)

