def merge_sort(the_list):
    if len(the_list) > 1:
        mid_point = len(the_list) // 2
        left = merge_sort(the_list[:mid_point])
        right = merge_sort(the_list[mid_point:])

        sorted_list = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1
        sorted_list += left[left_index:]
        sorted_list += right[right_index:]
        print(sorted_list)
        return sorted_list
    else:
        return the_list


the_list = [2, 3, 1, 0, 12, 5, 10, 7]
merge_sort(the_list)
# 1st call: left = [2, 3, 1, 0], right = [12, 5, 10, 7]
# 2nd call: left = [2, 3], right = [1, 0]
# 3rd call: left = [12, 5], right = [10, 7]
# 4th call: left = [2], right = [3]
# 5th call: left = [1], right = [0]
# 6th call: left = [12], right = [5]
# 7th call: left = [10], right = [7]
