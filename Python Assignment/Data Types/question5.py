
sample_string = 'abc'

if len(sample_string)<3:
	print(sample_string)
else:
	if sample_string[len(sample_string)-3:]=='ing':
		print(sample_string+'ly')
	else:
		print(sample_string+'ing')
