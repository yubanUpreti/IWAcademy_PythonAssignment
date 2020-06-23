dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}


for key,value in dic2.items():
	dic1[key]=value
for key,value in dic3.items():
	dic1[key]=value

print(dic1)