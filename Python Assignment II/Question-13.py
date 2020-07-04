import csv

tuples_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

def write_to_csv(filename,tuples):
	with open(filename,'w') as file:
		csvfile = csv.writer(file,delimiter=',')
		csvfile.writerow(('name', 'address', 'age'))
		for data in tuples:
			csvfile.writerow(data)
		print("CSV file successfully created ")

write_to_csv('test.csv',tuples_list)



