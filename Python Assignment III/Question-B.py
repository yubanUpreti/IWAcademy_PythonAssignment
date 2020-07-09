# Task to perform
# Inquiry
# Registration Rs 20000 Two installments available
# Display all Student information with paid and remaning
# Update Student Information
# Delete Student Information
# Return deposit amount Rs 20000 after course complete 

""" name, age, address, qualification, choosen_course, course_status, 
deposit_status, payment, installment = student attributes 

Here if installment is 0 then total of 20000 has been paid
if installment is 1 then total of 10000 has been paid and 10000 is remaning

"""


import csv
import os.path

class ITAcademy:
	""" Docstring for ITAcademy """
	def __init__(self):
		self.students_data = {} # Dictionary to hold student information
		self.courses = ['Python','Django','HTML','JavaScript'] # Course names

	def view_courses(self): # Display available courses
		print("")
		print(" Available Courses at ITAcademy ")
		print("")
		for i,course in enumerate(self.courses):
			print(f" {i} : {course}") 
		print("")

	def fee_info(self): # Display fee related information
		print("Fee Related FAQ ")
		print("")
		print("Registration Fee is Rs.20000. It can be paid in two installments of Rs. 10000 each. ")
		print("")

	def menu(self): # Display menu form which user can choose
		print("")
		print("*"*50)
		print("")
		print(" Welcome to ITAcademy Nepal ")
		print("*"*50)
		print("")
		print(" Please choose any option from below given choices ")
		print("")
		print("1. View Courses Information")
		print("2. View All Student Information")
		print("3. Course Registration")
		print("4. Update Student ")
		print("5. Detete Student ")
		print("6. Deposit Request ")
		print("7. Quit Application")
		print("")
		print("*"*50)

		return input(" Enter your choice : ") # return user choice 


class Student(ITAcademy):
	def __init__(self):
		super().__init__() # call ITAcademy constructor
		self.name = ''
		self.age = ''
		self.address = ''
		self.qualification = ''
		self.choosen_course = ''
		self.course_complete_status = 0 # Here 0 represents No and 1 represents Yes
		self.deposit_given_status = 0
		self.payment = 0
		self.installment = 2
	
	def insert_student(self): # get student information
		self.name = input('Enter your name: ')
		self.age = input('Enter your age : ')
		self.address = input('Enter your address : ')
		self.qualification = input('Enter your qualification : ')
		self.choosen_course = input('Enter your course : ')

	def registration(self): # register student for a course
		self.fee_info()
		print("")
		try:
			self.insert_student()
			while True:
				self.payment = int(input('Enter the amount you want to pay Rs. [20000/10000] : '))

				if isinstance(self.payment,int):
					if (self.payment) == 20000:
						self.installment = 0
						break
					elif (self.payment) == 10000:
						self.installment = 1
						break
					else:
						print(" You have entered incorrect amount ")
				else:
					raise ValueError 

		except ValueError as e:
			print("")
			print(f"String to Int conversion error occured from payment value.  {e}")
			print("")
		finally:
			if self.payment != 0:
				self.id = str(len(self.students_data)+1)
				self.students_data[self.id+self.name] = {'name':self.name,'age':self.age,'address':self.address,'course':self.choosen_course,'course_status':self.course_complete_status,'deposit_status':self.deposit_given_status,'payment':int(self.payment),'installment':self.installment}
			else:
				pass
		print("")

	def show_all_students(self): # Diplay all student information
		print("")
		print("|S/N|Name|Age|Address|Course|Course Competed Status| Deposit Status| Payment| Installment|")
		for i,data in enumerate(self.students_data):
			print("")
			print(f"|{i+1}|{self.students_data[data]['name']}|{self.students_data[data]['age']}|{self.students_data[data]['address']}|{self.students_data[data]['course']}|{self.students_data[data]['course_status']}|{self.students_data[data]['deposit_status']}|{self.students_data[data]['payment']}|{self.students_data[data]['installment']}|")
			print("")

	def update_student(self): # update student information
		print("")
		print("If you don't know the ID see it in all Students Information")
		print("")
		print("Fill the information below to make update for that student")
		print("")
		s_id = input("Enter Student ID : ")
		s_name = input("Enter Student Name : ")
		print("")
		if (s_id+s_name )in self.students_data.keys():
			self.students_data[s_id+s_name]['name'] = input('Enter your name: ')
			self.students_data[s_id+s_name]['age'] = input('Enter your age : ')
			self.students_data[s_id+s_name]['address'] = input('Enter your address : ')
			self.students_data[s_id+s_name]['qualification'] = input('Enter your qualification : ')
			self.students_data[s_id+s_name]['course'] = input('Enter your course : ')
			pay = input("Enter you payment: ")

			get_value = input(" Enter 1. if you add to your previous payment or Enter 2. if you want to replace that payment ? [1,2]")
			if int(get_value) == 1:
				self.students_data[s_id+s_name]['payment'] += int(pay)
				self.students_data[s_id+s_name]['installment'] = 0
			elif int(get_value) == 2:
				if int(pay) > 10000:
					self.students_data[s_id+s_name]['installment'] = 0
				else:
					self.students_data[s_id+s_name]['installment'] = 1
					self.students_data[s_id+s_name]['course_status'] = 0
					self.students_data[s_id+s_name]['deposit_status'] = 0

				self.students_data[s_id+s_name]['payment'] = int(pay)
			else:
				pass

			if int(self.students_data[s_id+s_name]['installment']) == 0:
				self.students_data[s_id+s_name]['course_status'] = input("Enter Course completion status [0: Incomplete , 1: Complete ")
				if int(self.students_data[s_id+s_name]['course_status']) == 1:
					self.students_data[s_id+s_name]['deposit_status'] = input("Enter Deposit Status : ")


		else:
			print(f"{s_id} {s_name} doesn't exist in the database")

	def delete_student(self):
		print("")
		print("Fill the information below to make update for that student")
		print("")
		s_id = input("Enter Student ID : ")
		s_name = input("Enter Student Name : ")
		print("")

		if (s_id+s_name )in self.students_data.keys():
			print(f"{s_name} data has been deleted ")
			del self.students_data[s_id+s_name]
		else:
			print(f"{s_id} {s_name} doesn't exist in the database")


	def return_deposit(self):
		print("")
		print("Fill the information below to make update for that student")
		print("")
		s_id = input("Enter Student ID : ")
		s_name = input("Enter Student Name : ")
		print("")

		if (s_id+s_name )in self.students_data.keys():
			if int(self.students_data[s_id+s_name]['installment']) == 0:
				if int(self.students_data[s_id+s_name]['course_status']) == 1 and int(self.students_data[s_id+s_name]['deposit_status']) == 1:

					print("Deposit has already been provided ..")

				elif int(self.students_data[s_id+s_name]['course_status']) == 1 and int(self.students_data[s_id+s_name]['deposit_status']) == 0:
					
					self.students_data[s_id+s_name]['deposit_status'] = 1
					print("Deposit has been processed sucessfully. ")

				else:
					self.students_data[s_id+s_name]['course_status'] = input("Enter Course completion status [0: Incomplete , 1: Complete ] : ")
					if int(self.students_data[s_id+s_name]['course_status']) == 1:
							self.students_data[s_id+s_name]['deposit_status'] = input("Enter Deposit Status : ")
							print("Deposit has been processed sucessfully. Funds will be made available soon ")
			else:
				print("You can't request deposit as your remaining installment is not done")
		else:
			print(f"{s_id} {s_name} doesn't exist in the database")


bool_value = True

s = Student() # create Student class object 
while bool_value:
	user_input = s.menu()
	if int(user_input) == 1:
		s.view_courses()
	elif int(user_input) == 2:
		s.show_all_students()
	elif int(user_input) == 3:
		s.registration()
	elif int(user_input) == 4:
		s.update_student()
	elif int(user_input) == 5:
		s.delete_student()
	elif int(user_input) == 6:
		s.return_deposit()
	elif int(user_input) == 7:
		print("")
		print(" Terminating Application ")
		print("")
		exist_file = os.path.isfile('ITAcademy_data.csv') # check if file exist in the directory
		with open('ITAcademy_data.csv', 'a') as csvfile:
			columns = ['Name','Age','Address','Course','Course Competed Status', 'Deposit Status', 'Payment', 'Installment']
			writer = csv.DictWriter(csvfile, fieldnames=columns)
			if not exist_file: # write header if its the first time only
				writer.writeheader()
			for i,key in enumerate(s.students_data.keys()):

				writer.writerow({'Name':s.students_data[key]['name'],'Age':s.students_data[key]['age'],'Address':s.students_data[key]['address'],'Course':s.students_data[key]['course'],'Course Competed Status':s.students_data[key]['course_status'], 'Deposit Status':s.students_data[key]['deposit_status'], 'Payment':s.students_data[key]['payment'], 'Installment':s.students_data[key]['installment']})

		print("Student Data has been written to csv file ")

		bool_value = False
	else:
		print("")
		print('You may have entered invalid option. Try Again')
		print("")
