fib = lambda n: 1 if n<=1 else fib(n-1)+fib(n-2)

for i in range(10):
	print(fib(i))