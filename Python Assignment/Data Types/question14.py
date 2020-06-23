def add_tags(tag,content):
	tag_statement = '<'+tag+'>'+content+'</'+tag+'>'
	return tag_statement

print(add_tags('i','Python'))
print(add_tags('b','Python is best'))