my_information = ('Youban','Uprety','26')
friend_1_information = ('Sagar','Dahal',None)
friend_2_information = ('Niroj','Koirala','24')
friend_3_information = ('Pratik','Upadhaya','29')

friend_test_list = []
print('')

friend_test_list.append(my_information)
friend_test_list.append(friend_1_information)
friend_test_list.append(friend_2_information)
friend_test_list.append(friend_3_information)

total = 0
for i in range(len(friend_test_list)):
		if friend_test_list[i][2] == None:
			continue
		else:
			total += int(friend_test_list[i][2])
get_avg = (round(total/len(friend_test_list),0))


for data in friend_test_list:

	if data[2] == None:
		print(f"{data[0]} {data[1]} --> Young")
		print("")
	else:
		print("")
		if int(data[2]) > get_avg:
			print(f"{data[0]} {data[1]} --> Old")
		else:
			print(f"{data[0]} {data[1]} --> Young")
		print("")



