check_number = lambda x: int(x)

try:
	sample_string = '1000'
	check_number(sample_string)
	print('String is integer value')
except ValueError as e:
	print(f'String is not a integer value. Error : {e} ')