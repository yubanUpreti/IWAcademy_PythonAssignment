square = lambda x: x**2

cube = lambda x: x**3

sample_list = [1,2,3,4,5]

squared_list = [square(x) for x in sample_list]
cubed_list = [cube(x) for x in sample_list]

print(squared_list)
print(cubed_list)