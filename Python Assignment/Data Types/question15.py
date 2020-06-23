def insert_string_middle(enclosure,string):
	to_put=int(len(enclosure)/2)
	print(enclosure[:to_put]+string+enclosure[-to_put:])


insert_string_middle('(())<<>>','hello')
insert_string_middle('{{}}','hello')
