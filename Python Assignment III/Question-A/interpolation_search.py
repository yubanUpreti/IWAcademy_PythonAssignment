print("#"*50)
print("")
print("*"*20+"  Interpolation Search  "+"*"*20)

def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index +(upper_bound_index - lower_bound_index) * (search_value - input_list[lower_bound_index]) //(input_list[upper_bound_index] - input_list[lower_bound_index])


def interpolation_search(ordered_list, term):

    size_of_list = len(ordered_list) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(ordered_list, index_of_first_element, index_of_last_element, term)

        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return -1

        if ordered_list[mid_point] == term:
            return mid_point

        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    if index_of_first_element > index_of_last_element:
        return None

random_numbers= [99,1,16,2,31]
search_value = 16
print(f" The index of {search_value} is {interpolation_search(sorted(random_numbers),search_value)}")
print("")
print("#"*50)