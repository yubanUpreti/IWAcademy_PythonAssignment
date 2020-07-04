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

		if not any(target_list):
			return "Valid Set of Parenthesis"
		else:
			return "Invalid Set of Parenthesis" 


test0 = check_validity('({[)]')
print(test0.verify())

test1 = check_validity('()[]{}')
print(test1.verify())

test2 = check_validity('{{{')
print(test2.verify())

test3 = check_validity('()')
print(test3.verify())

