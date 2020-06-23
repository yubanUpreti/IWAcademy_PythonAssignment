get_interger = lambda x: isinstance(x,int)

sample_list = [1,'a',8,'pep']

print(list(filter(get_interger,sample_list)))