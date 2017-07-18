the_list = [2, 3, 1, 0, 12, 5, 10, 7]

def selection_sort(the_list):
    for last_pos in range(len(the_list)-1, 0, -1):
        the_largest = the_list[0]
        for index in range(0, last_pos+1):
            if the_list[the_largest] < the_list[index]:
                the_largest = index
        temp = the_list[the_largest]
        the_list[the_largest] = the_list[last_pos]
        the_list[last_pos] = temp

    print(the_list)


selection_sort(the_list)
