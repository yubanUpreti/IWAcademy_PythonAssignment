from functools import reduce

sample_list = [1,2,3,10,100]  

def factorial(x,y):
	return x*y


print(reduce(factorial,sample_list))