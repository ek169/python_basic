def binary_search(the_list, element):
    min_index = 0
    max_index = len(the_list)

    while min_index < max_index:
        mid_point = (min_index+max_index-1) // 2
        if element > the_list[mid_point]:
            min_index = mid_point+1
        elif element < the_list[mid_point]:
            max_index = mid_point-1
        elif element is the_list[mid_point]:
            return True
    return False


the_list = [0, 2, 3, 5, 8, 13, 19, 31]

print(binary_search(the_list, 5) is True)
print(binary_search(the_list, 7) is False)
print(binary_search(the_list, 11) is False)
print(binary_search(the_list, 0) is True)
print(binary_search(the_list, -2) is False)
print(binary_search(the_list, 31) is True)
print(binary_search(the_list, 19) is True)
print(binary_search(the_list, 6) is False)
print(binary_search(the_list, 100) is False)




