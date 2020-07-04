
# Leap Year 

input_year = 2020

if ((input_year % 4 == 0) and (input_year % 100 != 0) )  or (input_year % 400 == 0):
	print(f'{input_year} is a Leap Year')
else:
	print(f'{input_year} is not a Leap Year')