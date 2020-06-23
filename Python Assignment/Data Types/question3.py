
sample_string = 'restart'
# sample_string = 'painterpaints'

# short_list = list(sample_string)[1:]

print(sample_string[0]+"".join([i if i!=sample_string[0] else '$' for i in list(sample_string)[1:]]))
