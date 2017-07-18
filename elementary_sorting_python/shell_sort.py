def shell_sort(the_list):
    increment = len(the_list) // 2
    while increment > 0:
        for next_subarray_to_sort in range(0, increment):
            for next_val in range(increment+next_subarray_to_sort, len(the_list), increment):
                for sorted_index in range(next_subarray_to_sort, next_val, increment):
                    if the_list[sorted_index] > the_list[next_val]:
                        temp = the_list[sorted_index]
                        the_list[sorted_index] = the_list[next_val]
                        the_list[next_val] = temp

        increment = increment // 2
        print(the_list)


the_list = [2, 3, 1, 0, 12, 5, 10, 7]
shell_sort(the_list)
