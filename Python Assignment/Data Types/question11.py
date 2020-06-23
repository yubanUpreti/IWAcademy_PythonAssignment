from collections import Counter

sample_string = 'python python program to count the occurrences of each word in a given sentence'
string_to_list = sample_string.split(' ')

print(Counter(string_to_list))