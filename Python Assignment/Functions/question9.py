def check_prime(n):
	for i in range(2,n):
		if n%i==0:
			print('Number is not Prime')
			break
		else:
			if i == n-1:
				print("Number is Prime")


check_prime(10)