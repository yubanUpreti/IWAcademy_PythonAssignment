sort_by_lambda = lambda x: sorted(x,key=lambda tup : tup[0])

sample_list = [(19,2),(11,9)]
print(sort_by_lambda(sample_list))

