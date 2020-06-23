
sample_string = 'The lyrics is not that poor!'
# sample_string = 'The lyrics is that poor!'

to_list = sample_string.split(' ')

if 'not' in to_list and to_list.index('not') < to_list.index('poor!'):
	remove_after_not = to_list[0:to_list.index('not')]
	remove_after_not.append('good!')
	print(" ".join(remove_after_not))
else:
	to_list.pop(to_list.index('poor!'))
	to_list.append('good!')
	print(" ".join(to_list))
