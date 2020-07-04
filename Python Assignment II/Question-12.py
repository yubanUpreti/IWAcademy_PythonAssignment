def is_palindrome(arg_string):
	if arg_string == arg_string[::-1]:
		print("Given String is Palindrome")
	else:
		print("Given String is not Palindrome")


is_palindrome('mom')
is_palindrome('happy')
