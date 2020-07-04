def is_prime(n):
	"""
	Checks if the given number is prime or not
	n: integer number as argument
	"""
	for i in range(2,n): # Runs the loop starting from 2 to n
		if n%i==0:
			return False
			break
		else:
			if i == n-1:
				return True


print(is_prime(10))