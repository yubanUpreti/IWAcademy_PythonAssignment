
sample_string = 'The lyrics is not that poor!'

to_list = sample_string.split(' ')

print(f"Longest word length : {max([len(i) for i in to_list])}")
