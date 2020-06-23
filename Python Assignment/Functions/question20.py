sample_list_one = [1,2,3,1]
sample_list_two = [1,2,4,3,1,8,9]

intersection_find = lambda x,y : [i for i in x if i in y]


print(intersection_find(sample_list_one,sample_list_two))
