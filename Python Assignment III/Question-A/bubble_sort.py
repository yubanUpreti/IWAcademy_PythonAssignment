print("#"*50)
print("")
print("*"*20+"  Bubble Sort  "+"*"*20)
print("")

random_numbers= [99,1,16,2,31]
x= random_numbers.copy()

def swap(num1,num2,i,j):
	x[i]= num2
	x[j] = num1

is_greater = lambda x,y:  True if x > y else False
[swap(x[j],x[j+1],j,j+1) if is_greater(x[j],x[j+1]) else swap(x[j+1],x[j],j,j+1) for i in range(len(x)) for j in range(len(x)-i-1)]

print(f" Before Bubble Sort : {random_numbers} ")
print("")
print(f" After  Bubble Sort : {x} ")

print("#"*50)