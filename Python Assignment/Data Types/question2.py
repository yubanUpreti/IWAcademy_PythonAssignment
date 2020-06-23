
sample_string = 'Python'
# sample_string = 'Py'
# sample_string = 'w'


if len(sample_string)<2:
	print("")
elif len(sample_string)<4:
	expected_result = sample_string[:2]+sample_string[(len(sample_string)-2):]
	print(expected_result)
else:
	expected_result = sample_string[:2]+sample_string[(len(sample_string)-2):]
	print(expected_result)