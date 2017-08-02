def changed_val(n, start_num, changed_index):
    the_list = [start_num]
    for addition in range(1, n):
        the_list.append(start_num+addition)
    the_list[changed_index] = float("inf")
    print(the_list)
    min_index = 0
    max_index = n
    while min_index < max_index:
        mid_point = (min_index + max_index) // 2
        print(min_index, max_index, mid_point)
        if (mid_point)*(the_list[min_index] + the_list[mid_point]) \
                is not ((start_num+mid_point)/2) + (start_num+mid_point + start_num+min_index):
            max_index = mid_point-1
        elif ((max_index-mid_point)/2)*(the_list[mid_point] + the_list[max_index]) \
                is not ((start_num+max_index-mid_point)/2) + (start_num+mid_point + start_num+max_index):
            min_index = mid_point+1
        elif the_list[mid_point] is not (start_num+mid_point):
            return mid_point
    return None

print(changed_val(10, 0, 3))
