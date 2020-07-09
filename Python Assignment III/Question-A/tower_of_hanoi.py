print("#"*50)
print("")
print("*"*20+" Tower of Hanoi problem for ‘n’ number of disks.  "+"*"*20)

def tower_of_hanoi(number_of_disks,src,dst,temp):
	if number_of_disks == 1: 
		print(f" Move disk {number_of_disks} from {src} to {dst} ")
		return 
	tower_of_hanoi(number_of_disks-1,src,dst,temp)
	print(f" Move disk {number_of_disks} from {src} to {dst} ")
	tower_of_hanoi(number_of_disks-1,temp,dst,src)
		 


tower_of_hanoi(3,'A','B','C')


print("")
print("#"*50)