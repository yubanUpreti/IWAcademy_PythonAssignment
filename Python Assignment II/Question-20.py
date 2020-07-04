class return_zero_sum:
	def __init__(self,arg_list):
		self.arg_list = arg_list
		self.result_list = []

	def get_list(self):
		for i in range(len(self.arg_list)):
			for j in range(i+1,len(self.arg_list)):
				for k in range(i+2,len(self.arg_list)):
					if (self.arg_list[i]+self.arg_list[j]+self.arg_list[k]) == 0:
						self.result_list.append([self.arg_list[i],self.arg_list[j],self.arg_list[k]])
		return self.result_list


test = return_zero_sum([-25, -10, -7, -3, 2, 4, 8, 10])

print(test.get_list())