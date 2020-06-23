
sample_string = 'IWAcademy'
string_to_list = list(sample_string)
new_string=''

for i,x in enumerate(string_to_list):
	if i%2==0:
		new_string+=sample_string[i] 
	else:
		continue
print(new_string)