calulator_functions = {'+':lambda x,y: x+y , '-':lambda x,y: x-y , '*':lambda x,y: x*y , '/':lambda x,y: x/y , '**':lambda x,y: x**y }

operator_choice = ['Addition : +','Subtaction : -','Multiplication : *','Division : /','Power : **']
try:
	print("Your Operator Choices")
	print(operator_choice)
	print("")
	x_value = int(input('Enter First Number: '))
	y_value = int(input('Enter Second Number: '))
	if isinstance(x_value,int)  and isinstance(y_value,int):
		operator = (input('Enter Operator from above choices : '))
		result = calulator_functions[operator]((x_value),(y_value))
		print("")
		print(f" Obtained Result : {result} ")
	else:
		raise ValueError
except ZeroDivisionError as er:
	print(f"You have tried to divide a number by zero. {er}")
except ValueError as er:
	print(f'Error : integer value not entered {er} ')
except Exception as er:
	print(er)
finally:
	print("Thank you. Have a good day")