import csv

dict_listdata = []

def read_from_csv(filename,dict_listdata):
	with open(filename,'rt') as file:
		csvfile = csv.reader(file)
		for i,data in enumerate(csvfile):
			if i == 0 or data == []:
				continue
			else:
				dict_data = {}
				dict_data['name'] = data[0]
				dict_data['address'] = data[1]
				dict_data['age'] = data[2]
				dict_listdata.append(dict_data)

		print("CSV file read successfully  ")

read_from_csv('test.csv',dict_listdata)

print(dict_listdata)



