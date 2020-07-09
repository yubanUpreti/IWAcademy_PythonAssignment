print("#"*50)
print("")
print("*"*20+"  Insertion Sort  "+"*"*20)

random_numbers= [99,1,16,2,31]
x = random_numbers.copy()
def swap2(value,j):
	while j>0 and x[j-1] > value:
		x[j]=x[j-1]
		j=j-1
	x[j] = value

[swap2(x[i],i) for i in range(1,len(x))] 

print(f" Before Insertion Sort : {random_numbers} ")
print("")
print(f" After  Insertion Sort : {x} ")

print("")
print("#"*50)