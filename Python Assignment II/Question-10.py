import re

def ConvertCamelCase(sep,arg_string):
	wordList = re.findall('[A-Z][^A-Z]*' ,arg_string)
	print(f"{sep}".join([x.lower() for x in wordList]))



ConvertCamelCase('-','ThisIsCamelCased')
ConvertCamelCase('_','ThisIsCamelCased')