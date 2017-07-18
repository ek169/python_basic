the_list = [2, 3, 1, 0, 12, 5, 10, 7]

def bubble_sort(the_list):
    no_exchanges = False
    while not no_exchanges:
        no_exchanges = True
        for n in range(0, len(the_list)-1):
            if the_list[n] > the_list[n+1]:
                no_exchanges = False
                temp = the_list[n]
                the_list[n] = the_list[n+1]
                the_list[n+1] = temp


    print(the_list)

bubble_sort(the_list)