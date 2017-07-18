def quick_sort(the_list):
    if len(the_list) > 1:
        pivot = the_list[0]
        left_mark = 1
        right_mark = len(the_list)-1
        while left_mark <= right_mark:
            if the_list[left_mark] < pivot:
                left_mark += 1
            else:
                if the_list[right_mark] < pivot:
                    temp = the_list[left_mark]
                    the_list[left_mark] = the_list[right_mark]
                    the_list[right_mark] = temp
                right_mark -= 1

        temp = the_list[0]
        the_list[0] = the_list[right_mark]
        the_list[right_mark] = temp

        left = quick_sort(the_list[:right_mark])
        right = quick_sort(the_list[left_mark:])
        the_list[:right_mark] = left
        the_list[left_mark:] = right

        return the_list

    return the_list


the_list = [2, 3, 1, 0, 12, 5, 10, 7]
print(quick_sort(the_list))
