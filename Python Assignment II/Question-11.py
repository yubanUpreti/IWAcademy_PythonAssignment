filename = 'README.txt'

# Case 1

print(f" FileName --> {filename.split('.')[0]}, Extension --> .{filename.split('.')[1]}")


# Case 2
get_index = filename.find('.')
print(f" FileName --> {filename[0:get_index]}, Extension --> {filename[get_index:]}")
