
sample_string = 'IWAcademy'
nth_character_remove = 5

if not sample_string:
	print("Sample String is Empty")
else:
	string_to_list=list(sample_string)
	string_to_list.pop(nth_character_remove)
	print(f'After {nth_character_remove}th character removed word becomes : {"".join(string_to_list)}')
