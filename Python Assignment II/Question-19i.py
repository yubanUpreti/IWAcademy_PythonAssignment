class check_validity:
	def __init__(self,parenthesis_string):
		self.arg_string = parenthesis_string
		self.string_to_list = list(self.arg_string)
	def verify(self):
		target_list = self.string_to_list.copy()
		dictionary_parenthesis = {'{':'}','}':'{',')':'(','(':')',']':'[','[':']'}
		for i in range(len(self.string_to_list)):
				if dictionary_parenthesis[self.string_to_list[i]] in self.string_to_list:
					idx = self.string_to_list.index(dictionary_parenthesis[self.string_to_list[i]])

					target_list[idx] = 0
					target_list[i] = 0

		if len( set( target_list ) ) == 1:
			return "Valid Set of Parenthesis"
		else:
			return "Invalid Set of Parenthesis" 


test = check_validity('({[)]')
print(test.verify())

test = check_validity('()[]{}')
print(test.verify())

test = check_validity('{{{')
print(test.verify())

test = check_validity('()')
print(test.verify())


	# def verify(self):
	# 	target_list = [1]*len(self.string_to_list)
	# 	dictionary_parenthesis = {'{':'}','}':'{',')':'(','(':')',']':'[','[':']'}
	# 	for i in range(len(self.string_to_list)):
	# 		for j in range(len(self.string_to_list)):
	# 			if self.string_to_list[i] != self.string_to_list[j] and i != j:
	# 				target_list[i] = 0

	# 	print(target_list)