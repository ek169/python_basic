the_list = [2, 3, 1, 0, 12, 5, 10, 7]

def insertion_sort(the_list):
    for next_item_to_sort in range(1, len(the_list)):
        for sorted_index in range(0, next_item_to_sort):
            if the_list[next_item_to_sort] < the_list[sorted_index]:
                the_list.insert(sorted_index, the_list.pop(next_item_to_sort))
                # print(the_list[0:next_item_to_sort]) - to see growth of sublist
    print(the_list)

insertion_sort(the_list)
