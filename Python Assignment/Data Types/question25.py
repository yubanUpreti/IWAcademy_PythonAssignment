items_in_list = [{},{},{}]


def check_list(data_as_list):
	if not data_as_list:
		return True
	else:
		for data in data_as_list:
			if not data:
				continue
			else:
				return False
		return True

print(check_list(items_in_list))
