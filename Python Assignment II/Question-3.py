
# Anagrams

paragraph = " I love coding in python "

word_list = paragraph.lower().rstrip().lstrip().split(' ')

for word in word_list:
	for i in range(len(word_list)):
		if (word in word_list[i]) and (word != word_list[i]):
			print(f'Anagram *{word}* can be generated from  --->> *{word_list[i]}* ')
		else:
			continue	