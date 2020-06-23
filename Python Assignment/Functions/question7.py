sample_string = 'The quick Brow Fox'

def count_up_low(sample_string):
	upper_count = 0
	lower_count = 0
	for val in list(sample_string):
		if val.isupper():
			upper_count +=1
		elif val.islower():
			lower_count += 1
		else:
			continue
	print(f'Number of Uppercase Letter : {upper_count}')
	print(f'Number of Lowercase Letter : {lower_count}')



count_up_low(sample_string)