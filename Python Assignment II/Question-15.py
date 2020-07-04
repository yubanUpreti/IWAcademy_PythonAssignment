class Bank:
	pass

class Customer(Bank):
	"""
	Customer Class of a Bank
	"""
	def __init__(self,name,address):
		super().__init__()

		self.name = name
		self.address = address
		# self.phone = a
		# self.birthday = a 
		# self.citizenship_number = a 
		# self.relationship_status = a
		# self.beneficiary_name = a
		# self.beneficiary_citzenship_number = a 
		# self.current_balance = a
		# self.account_opening_date = a 
		# self.account_number = a
		# self.account_type = a

	def withdraw(self):
		pass
	def deposit(self):
		pass
	def transfer(self):
		pass
	def change(self):
		pass


c = Customer('Youban Uprety','KTM',)

print(c.name)